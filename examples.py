"""
Example usage of the GatewayzApi Python SDK.

This file demonstrates common patterns for using the SDK.
"""

import asyncio
from gatewayz import GatewayzApi, AsyncGatewayzApi
from gatewayz.types import Message
from gatewayz.core import ApiError


# Example 1: Basic synchronous client usage
def basic_example():
    """Basic synchronous client usage."""
    client = GatewayzApi(
        token="YOUR_API_TOKEN",
        base_url="https://api.gatewayz.ai"
    )

    # Health check
    try:
        health = client.health_check_health_get()
        print(f"Health check: {health}")
    except ApiError as e:
        print(f"API Error: {e.status_code} - {e.body}")


# Example 2: Chat completions
def chat_example():
    """Chat completions example."""
    client = GatewayzApi(
        token="YOUR_API_TOKEN",
        base_url="https://api.gatewayz.ai"
    )

    # Send a chat message
    response = client.chat.chat_completions(
        model="gpt-4",
        messages=[
            Message(role="system", content="You are a helpful assistant."),
            Message(role="user", content="What is the capital of France?")
        ],
        max_tokens=100,
        temperature=0.7
    )
    print(f"Chat response: {response}")


# Example 3: Async usage
async def async_example():
    """Async client usage example."""
    client = AsyncGatewayzApi(
        token="YOUR_API_TOKEN",
        base_url="https://api.gatewayz.ai"
    )

    # Concurrent requests
    health_task = client.health_check_health_get()
    ping_task = client.ping_ping_get()

    health, ping = await asyncio.gather(health_task, ping_task)
    print(f"Health: {health}")
    print(f"Ping: {ping}")


# Example 4: User registration and authentication
def auth_example():
    """Authentication example."""
    from gatewayz.types import UserRegistrationRequest

    client = GatewayzApi(
        token="YOUR_API_TOKEN",
        base_url="https://api.gatewayz.ai"
    )

    # Register a new user
    try:
        user = client.authentication.register_user(
            request=UserRegistrationRequest(
                email="newuser@example.com",
                # Add other required fields based on your API
            )
        )
        print(f"User registered: {user}")

        # Get user profile
        profile = client.authentication.get_profile()
        print(f"Profile: {profile}")
    except ApiError as e:
        print(f"Authentication error: {e}")


# Example 5: Plans and subscriptions
def subscription_example():
    """Plans and subscription example."""
    client = GatewayzApi(
        token="YOUR_API_TOKEN",
        base_url="https://api.gatewayz.ai"
    )

    # List available plans
    plans = client.plans.list_plans()
    print(f"Available plans: {plans}")

    # Get current subscription
    subscription = client.subscription.get_subscription()
    print(f"Current subscription: {subscription}")


# Example 6: Coupon management
def coupon_example():
    """Coupon management example."""
    client = GatewayzApi(
        token="YOUR_API_TOKEN",
        base_url="https://api.gatewayz.ai"
    )

    # List available coupons
    coupons = client.coupons.list_available_coupons()
    print(f"Available coupons: {coupons}")

    # Redeem a coupon
    try:
        redemption = client.coupons.redeem_coupon(coupon_code="SAVE20")
        print(f"Coupon redeemed: {redemption}")
    except ApiError as e:
        print(f"Coupon error: {e}")


# Example 7: Error handling
def error_handling_example():
    """Comprehensive error handling example."""
    from gatewayz.errors import UnprocessableEntityError

    client = GatewayzApi(
        token="YOUR_API_TOKEN",
        base_url="https://api.gatewayz.ai"
    )

    try:
        response = client.chat.chat_completions(
            model="gpt-4",
            messages=[
                Message(role="user", content="Hello!")
            ]
        )
        print(f"Success: {response}")
    except UnprocessableEntityError as e:
        print(f"Validation error: {e}")
    except ApiError as e:
        print(f"API error: {e.status_code} - {e.body}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Example 8: Custom configuration
def custom_config_example():
    """Custom configuration example."""
    import httpx

    # Custom httpx client with specific settings
    custom_httpx = httpx.Client(
        timeout=120.0,
        follow_redirects=True,
        verify=True
    )

    client = GatewayzApi(
        token="YOUR_API_TOKEN",
        base_url="https://api.gatewayz.ai",
        httpx_client=custom_httpx,
        headers={
            "X-Custom-Header": "custom-value"
        }
    )

    response = client.ping_ping_get()
    print(f"Response: {response}")


# Example 9: Using request options
def request_options_example():
    """Request options example."""
    from gatewayz.core import RequestOptions

    client = GatewayzApi(
        token="YOUR_API_TOKEN",
        base_url="https://api.gatewayz.ai"
    )

    # Custom request options
    response = client.ping_ping_get(
        request_options=RequestOptions(
            timeout_in_seconds=30,
            max_retries=3,
            additional_headers={"X-Request-ID": "abc123"}
        )
    )
    print(f"Response: {response}")


# Example 10: Dynamic token provider
def dynamic_token_example():
    """Dynamic token provider example."""

    def get_token():
        # Your logic to fetch or refresh token
        # This could read from a file, environment variable, or API
        return "dynamically-fetched-token"

    client = GatewayzApi(
        token=get_token,  # Pass callable instead of string
        base_url="https://api.gatewayz.ai"
    )

    response = client.ping_ping_get()
    print(f"Response: {response}")


if __name__ == "__main__":
    print("GatewayzApi SDK Examples")
    print("=" * 50)

    # Uncomment the examples you want to run
    # basic_example()
    # chat_example()
    # asyncio.run(async_example())
    # auth_example()
    # subscription_example()
    # coupon_example()
    # error_handling_example()
    # custom_config_example()
    # request_options_example()
    # dynamic_token_example()

    print("\nPlease uncomment the examples you want to run and add your API credentials.")
