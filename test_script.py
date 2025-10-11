from gatewayz import GatewayzApi

# Initialize the client
client = GatewayzApi(
    token="gw_live_t4EZuoGXOD312rKKEGWyeAhphpfx7bHinzqAvh2cNI4",
    base_url="https://api.gatewayz.ai"
)

# Health check
response = client.health_check_health_get()
print(response)

# Ping endpoint
pong = client.ping_ping_get()
print(pong)
