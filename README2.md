```mermaid
flowchart
subgraph Manufacturing Site Network
    S[IoT Error Log Producer 1] -->|Publish| Z
    T[IoT Error Log Producer 2] -->|Publish| Z
    Y[IoT Error Log Producer N] -->|Publish| Z
    subgraph Gogent
        subgraph embedded NATS
            Z@{ shape: das, label: "agent.technical.support" }
            U@{ shape: lin-cyl, label: "JetStream Persistence" }
        end
        Z -->|Subscribe| A{Agent Sig}
        E[(Error Log DB)]
        A --> |Retain w/ policy conditions| E
    end
    subgraph LLM Providers
        A -->|Request| L[LLM API]
        L -->|Response| A
        subgraph "Available Providers"
            L1[Ollama (default)]
            L2[OpenAI]
            L3[Azure OpenAI]
            L4[Azure AD]
            L5[Cloudflare Azure]
            L6[Gemini]
            L7[Claude]
            L8[DeepSeek]
        end
    end
end

```
