# Architecture Diagrams and Technical Designs

## 1. Direct MCP-Server Connections Architecture

### High-Level Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                         MCP Client                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Connection Manager                            │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐             │  │
│  │  │ Server A │ │ Server B │ │ Server C │ ...         │  │
│  │  │ Config   │ │ Config   │ │ Config   │             │  │
│  │  └──────────┘ └──────────┘ └──────────┘             │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
         │              │              │
         │ MCP          │ MCP          │ MCP
         │ Protocol     │ Protocol     │ Protocol
         ▼              ▼              ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ MCP Server A │ │ MCP Server B │ │ MCP Server C │
│              │ │              │ │              │
│ Tools:       │ │ Tools:       │ │ Tools:       │
│ - Tool A1    │ │ - Tool B1    │ │ - Tool C1    │
│ - Tool A2    │ │ - Tool B2    │ │ - Tool C2    │
│              │ │              │ │              │
│ Auth: API    │ │ Auth: OAuth  │ │ Auth: mTLS   │
│ Key          │ │              │ │              │
└──────────────┘ └──────────────┘ └──────────────┘
```

### Connection Flow
```
Client Request Flow:
1. Client → [Select Server] → Server Config
2. Client → [Establish Connection] → Server Transport (HTTP/WebSocket)
3. Client → [Authenticate] → Server Auth Mechanism
4. Client → [Send MCP Request] → Server Handler
5. Server → [Process Request] → Tool/Resource/Prompt
6. Server → [Send MCP Response] → Client
7. Client → [Process Response] → Application Logic

Error Handling:
- Connection Failure → Retry Logic (per-server)
- Auth Failure → Credential Refresh (per-server)
- Timeout → Circuit Breaker (per-server)
- Server Error → Fallback Logic (application-specific)
```

### Configuration Structure
```json
{
  "mcpServers": {
    "server-a": {
      "url": "https://api.example.com/mcp",
      "transport": "http",
      "auth": {
        "type": "apiKey",
        "header": "X-API-Key",
        "value": "${SERVER_A_API_KEY}"
      },
      "timeout": 30000,
      "retries": 3,
      "circuitBreaker": {
        "threshold": 5,
        "timeout": 60000
      }
    },
    "server-b": {
      "url": "wss://mcp.service-b.com",
      "transport": "websocket",
      "auth": {
        "type": "oauth2",
        "tokenUrl": "https://auth.service-b.com/token",
        "clientId": "${SERVER_B_CLIENT_ID}",
        "clientSecret": "${SERVER_B_CLIENT_SECRET}"
      },
      "timeout": 45000,
      "retries": 2
    },
    "server-c": {
      "url": "https://internal.example.com:8443/mcp",
      "transport": "http",
      "auth": {
        "type": "mtls",
        "cert": "/path/to/client.crt",
        "key": "/path/to/client.key",
        "ca": "/path/to/ca.crt"
      },
      "timeout": 20000,
      "retries": 1
    }
  }
}
```

---

## 2. Centralized Gateway Architecture

### High-Level Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                         MCP Client                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Gateway Client SDK                            │  │
│  │  - Single endpoint configuration                      │  │
│  │  - Authentication token                               │  │
│  │  - Request/response handling                          │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ MCP Protocol + Gateway Extensions
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    MCP Gateway (HA)                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Gateway Core Components                  │  │
│  │  ┌────────────┐ ┌──────────┐ ┌──────────────────┐   │  │
│  │  │ Auth       │ │ Router   │ │ Service          │   │  │
│  │  │ Manager    │ │          │ │ Discovery        │   │  │
│  │  └────────────┘ └──────────┘ └──────────────────┘   │  │
│  │  ┌────────────┐ ┌──────────┐ ┌──────────────────┐   │  │
│  │  │ Connection │ │ Rate     │ │ Observability    │   │  │
│  │  │ Pool       │ │ Limiter  │ │ (Logs/Metrics)   │   │  │
│  │  └────────────┘ └──────────┘ └──────────────────┘   │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
         │              │              │
         │ MCP          │ MCP          │ MCP
         │ Protocol     │ Protocol     │ Protocol
         ▼              ▼              ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ MCP Server A │ │ MCP Server B │ │ MCP Server C │
│ (Backend)    │ │ (Backend)    │ │ (Backend)    │
└──────────────┘ └──────────────┘ └──────────────┘
```

### Gateway Request Flow
```
Client Request Flow:
1. Client → [Gateway Auth] → JWT/API Key Validation
2. Gateway → [Authorization Policy] → RBAC/ABAC Check
3. Gateway → [Rate Limiting] → Request Quota Check
4. Gateway → [Service Discovery] → Resolve Target Server
5. Gateway → [Load Balancing] → Select Server Instance
6. Gateway → [Connection Pool] → Get/Create Server Connection
7. Gateway → [Backend Auth] → Authenticate to Server
8. Gateway → [Forward Request] → MCP Server Handler
9. Server → [Process Request] → Tool/Resource/Prompt
10. Server → [Response] → Gateway
11. Gateway → [Response Transform] → Add Metadata/Tracing
12. Gateway → [Metrics/Logging] → Record Request
13. Gateway → [Send Response] → Client

Error Handling:
- Gateway Auth Failure → 401 Unauthorized
- Authorization Failure → 403 Forbidden
- Rate Limit Exceeded → 429 Too Many Requests
- Backend Unavailable → Retry/Circuit Breaker → 503 Service Unavailable
- Backend Error → Transform Error → Client
```

### Gateway Components Detail

#### Authentication Manager
```
┌─────────────────────────────────────┐
│     Authentication Manager          │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ Token Validation               │ │
│  │ - JWT verification             │ │
│  │ - API key lookup               │ │
│  │ - OAuth token introspection    │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Session Management             │ │
│  │ - Session store (Redis)        │ │
│  │ - Session timeout              │ │
│  │ - Refresh token handling       │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Backend Credential Management  │ │
│  │ - Secret storage (Vault)       │ │
│  │ - Credential rotation          │ │
│  │ - Per-backend auth             │ │
│  └───────────────────────────────┘ │
└─────────────────────────────────────┘
```

#### Router and Service Discovery
```
┌─────────────────────────────────────┐
│     Router & Service Discovery      │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ Service Registry               │ │
│  │ - Consul / Eureka / etcd       │ │
│  │ - Health checks                │ │
│  │ - Server metadata              │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Routing Rules                  │ │
│  │ - Path-based routing           │ │
│  │ - Header-based routing         │ │
│  │ - Version routing              │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Load Balancing                 │ │
│  │ - Round-robin                  │ │
│  │ - Least connections            │ │
│  │ - Weighted distribution        │ │
│  └───────────────────────────────┘ │
└─────────────────────────────────────┘
```

#### Observability Stack
```
┌─────────────────────────────────────┐
│        Observability                │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ Distributed Tracing            │ │
│  │ - OpenTelemetry                │ │
│  │ - Trace ID propagation         │ │
│  │ - Jaeger/Zipkin backend        │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Metrics Collection             │ │
│  │ - Request rate/latency         │ │
│  │ - Error rates                  │ │
│  │ - Backend health               │ │
│  │ - Prometheus export            │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Logging                        │ │
│  │ - Structured logs              │ │
│  │ - Request/response logging     │ │
│  │ - ELK/Loki aggregation         │ │
│  └───────────────────────────────┘ │
└─────────────────────────────────────┘
```

### Gateway Configuration
```yaml
# gateway-config.yaml
gateway:
  server:
    host: 0.0.0.0
    port: 8080
    tls:
      enabled: true
      cert: /etc/gateway/tls/server.crt
      key: /etc/gateway/tls/server.key

  authentication:
    providers:
      - type: jwt
        issuer: https://auth.example.com
        audience: mcp-gateway
        jwksUrl: https://auth.example.com/.well-known/jwks.json
      - type: apiKey
        header: X-API-Key
        storage: redis://auth-cache:6379/0

  authorization:
    type: rego  # Open Policy Agent
    policyPath: /etc/gateway/policies/
    defaultAllow: false

  rateLimiting:
    enabled: true
    storage: redis://rate-limit:6379/1
    limits:
      - matcher: user
        requests: 1000
        window: 60s
      - matcher: apiKey
        requests: 10000
        window: 60s

  backends:
    serviceDiscovery:
      type: consul
      address: consul:8500
      datacenter: dc1
    
    connectionPool:
      maxIdleConns: 100
      maxOpenConns: 200
      connMaxLifetime: 300s

    loadBalancing:
      algorithm: leastConn
      healthCheck:
        interval: 10s
        timeout: 5s
        unhealthyThreshold: 3

  observability:
    tracing:
      enabled: true
      exporter: jaeger
      endpoint: http://jaeger:14268/api/traces
      samplingRate: 0.1
    
    metrics:
      enabled: true
      exporter: prometheus
      path: /metrics
      port: 9090
    
    logging:
      level: info
      format: json
      output: stdout
```

---

## 3. Discovery Mechanisms Detail

### Direct Connection Discovery
```
Static Configuration:
┌──────────────┐
│ Client       │
│ Config File  │
│              │
│ servers:     │
│   - url: ... │
│   - url: ... │
└──────────────┘
        │
        ▼
┌──────────────┐
│ Application  │
│ Startup      │
│              │
│ Load servers │
│ Initialize   │
│ connections  │
└──────────────┘

Environment-Based:
┌──────────────┐
│ Environment  │
│ Variables    │
│              │
│ SERVER_A_URL │
│ SERVER_B_URL │
└──────────────┘
        │
        ▼
┌──────────────┐
│ Dynamic      │
│ Config       │
│ Builder      │
└──────────────┘
```

### Gateway Discovery
```
Service Registry Pattern:
┌──────────────┐     ┌──────────────┐
│ MCP Server A │────▶│  Service     │
│ (Register)   │     │  Registry    │
└──────────────┘     │  (Consul)    │
                     │              │
┌──────────────┐     │  - Server A  │
│ MCP Server B │────▶│  - Server B  │
│ (Register)   │     │  - Server C  │
└──────────────┘     └──────────────┘
                            │
                            │ Query
                            ▼
                     ┌──────────────┐
                     │   Gateway    │
                     │   Router     │
                     └──────────────┘

DNS-Based Discovery:
┌──────────────┐
│     DNS      │
│   _mcp._tcp  │
│   .service   │
│   .consul    │
└──────────────┘
        │
        │ SRV Lookup
        ▼
┌──────────────┐
│   Gateway    │
│   Discovers: │
│   - IP:Port  │
│   - Priority │
│   - Weight   │
└──────────────┘
```

---

## 4. Authorization Patterns

### Direct Connection Authorization
```
Per-Server Auth:
┌──────────────┐      ┌──────────────┐
│   Client     │      │  Server A    │
│              │─────▶│  Auth: API   │
│ Credentials: │      │  Key         │
│ - Key A      │      └──────────────┘
│ - Token B    │      ┌──────────────┐
│ - Cert C     │─────▶│  Server B    │
└──────────────┘      │  Auth: OAuth │
                      └──────────────┘
                      ┌──────────────┐
                      │  Server C    │
                      │  Auth: mTLS  │
                      └──────────────┘
```

### Gateway Authorization
```
Centralized Policy:
┌──────────────┐
│   Client     │
│   Token      │
└──────────────┘
        │
        ▼
┌──────────────────────────────┐
│      Gateway Auth            │
│  ┌────────────────────────┐  │
│  │  1. Validate Token     │  │
│  └────────────────────────┘  │
│  ┌────────────────────────┐  │
│  │  2. Extract Claims     │  │
│  │     - user_id          │  │
│  │     - roles            │  │
│  │     - permissions      │  │
│  └────────────────────────┘  │
│  ┌────────────────────────┐  │
│  │  3. Check Policy (OPA) │  │
│  │     allow if:          │  │
│  │       user.role ==     │  │
│  │         "admin"        │  │
│  └────────────────────────┘  │
│  ┌────────────────────────┐  │
│  │  4. Backend Auth       │  │
│  │     Get credentials    │  │
│  │     from Vault         │  │
│  └────────────────────────┘  │
└──────────────────────────────┘
        │
        ▼
┌──────────────┐
│ MCP Server   │
└──────────────┘
```

---

## 5. Observability Architecture

### Direct Connection Observability
```
Distributed Collection:
┌─────────────┐  Logs    ┌─────────────┐
│  Client     │─────────▶│  Log        │
│  Logger     │          │  Aggregator │
└─────────────┘          │  (ELK)      │
                         └─────────────┘

┌─────────────┐  Metrics ┌─────────────┐
│  Server A   │─────────▶│  Prometheus │
│  /metrics   │          │             │
└─────────────┘          └─────────────┘

┌─────────────┐  Traces  ┌─────────────┐
│  Server B   │─────────▶│   Jaeger    │
│  Tracing    │          │             │
└─────────────┘          └─────────────┘

Challenge: Correlation across sources
```

### Gateway Observability
```
Centralized Collection:
┌─────────────┐
│   Client    │
└─────────────┘
        │
        ▼
┌──────────────────────────────┐
│         Gateway              │
│  ┌────────────────────────┐  │
│  │  Request Interceptor   │  │
│  │  - Generate Trace ID   │  │
│  │  - Start timer         │  │
│  │  - Log request         │  │
│  └────────────────────────┘  │
│           │                  │
│           ▼                  │
│  ┌────────────────────────┐  │
│  │  Forward to Backend    │  │
│  │  + Trace headers       │  │
│  └────────────────────────┘  │
│           │                  │
│           ▼                  │
│  ┌────────────────────────┐  │
│  │  Response Interceptor  │  │
│  │  - Stop timer          │  │
│  │  - Log response        │  │
│  │  - Record metrics      │  │
│  │  - Export trace        │  │
│  └────────────────────────┘  │
└──────────────────────────────┘
        │
        ▼
┌─────────────────────────────┐
│   Observability Backend     │
│  - Unified logs             │
│  - Correlated traces        │
│  - Gateway + backend metrics│
└─────────────────────────────┘
```

---

## 6. High Availability Patterns

### Gateway HA Architecture
```
┌─────────────────────────────────────────────┐
│          Client Applications                │
└─────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│        Load Balancer (L7)                   │
│        - Health checks                      │
│        - SSL termination                    │
└─────────────────────────────────────────────┘
        │                │               │
        ▼                ▼               ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  Gateway    │  │  Gateway    │  │  Gateway    │
│  Instance 1 │  │  Instance 2 │  │  Instance 3 │
│  (Active)   │  │  (Active)   │  │  (Active)   │
└─────────────┘  └─────────────┘  └─────────────┘
        │                │               │
        └────────────────┴───────────────┘
                         │
                         ▼
        ┌────────────────────────────────┐
        │    Shared State (Redis)        │
        │    - Session store             │
        │    - Rate limit counters       │
        │    - Service registry cache    │
        └────────────────────────────────┘
                         │
                         ▼
        ┌────────────────────────────────┐
        │    Backend MCP Servers         │
        │    (with own HA strategy)      │
        └────────────────────────────────┘
```

This comprehensive architecture documentation provides detailed technical designs for both approaches, enabling informed decision-making for MCP server connectivity strategies.
