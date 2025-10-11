#!/usr/bin/env python3
"""
Quick test script to verify the gatewayz SDK is installed correctly.
Run this after installing with: pip install -e .
"""

def test_import():
    """Test that the main package can be imported."""
    try:
        import gatewayz
        print("✓ Successfully imported gatewayz package")
        return True
    except ImportError as e:
        print(f"✗ Failed to import gatewayz package: {e}")
        return False


def test_client_import():
    """Test that the main client classes can be imported."""
    try:
        from gatewayz import GatewayzApi, AsyncGatewayzApi
        print("✓ Successfully imported GatewayzApi and AsyncGatewayzApi")
        return True
    except ImportError as e:
        print(f"✗ Failed to import client classes: {e}")
        return False


def test_types_import():
    """Test that type definitions can be imported."""
    try:
        from gatewayz.types import Message, ChatSession, UserProfileResponse
        print("✓ Successfully imported type definitions")
        return True
    except ImportError as e:
        print(f"✗ Failed to import types: {e}")
        return False


def test_client_instantiation():
    """Test that the client can be instantiated."""
    try:
        from gatewayz import GatewayzApi
        client = GatewayzApi(
            token="test-token",
            base_url="https://test.example.com"
        )
        print("✓ Successfully instantiated GatewayzApi client")
        print(f"  Client type: {type(client)}")
        return True
    except Exception as e:
        print(f"✗ Failed to instantiate client: {e}")
        return False


def test_client_properties():
    """Test that client properties are accessible."""
    try:
        from gatewayz import GatewayzApi
        client = GatewayzApi(
            token="test-token",
            base_url="https://test.example.com"
        )

        # Test accessing sub-clients
        _ = client.chat
        _ = client.authentication
        _ = client.providers
        _ = client.models

        print("✓ Successfully accessed client properties")
        return True
    except Exception as e:
        print(f"✗ Failed to access client properties: {e}")
        return False


def test_async_client():
    """Test that async client can be imported and instantiated."""
    try:
        from gatewayz import AsyncGatewayzApi
        client = AsyncGatewayzApi(
            token="test-token",
            base_url="https://test.example.com"
        )
        print("✓ Successfully instantiated AsyncGatewayzApi client")
        return True
    except Exception as e:
        print(f"✗ Failed with async client: {e}")
        return False


def test_error_classes():
    """Test that error classes can be imported."""
    try:
        from gatewayz.errors import UnprocessableEntityError
        from gatewayz.core import ApiError
        print("✓ Successfully imported error classes")
        return True
    except ImportError as e:
        print(f"✗ Failed to import error classes: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("Testing gatewayz SDK Installation")
    print("=" * 60)
    print()

    tests = [
        test_import,
        test_client_import,
        test_types_import,
        test_client_instantiation,
        test_client_properties,
        test_async_client,
        test_error_classes,
    ]

    results = []
    for test in tests:
        result = test()
        results.append(result)
        print()

    print("=" * 60)
    passed = sum(results)
    total = len(results)

    if passed == total:
        print(f"✓ All {total} tests passed! SDK is installed correctly.")
        print()
        print("You can now use the SDK:")
        print()
        print("  from gatewayz import GatewayzApi")
        print()
        print("  client = GatewayzApi(")
        print("      token='YOUR_TOKEN',")
        print("      base_url='https://your-api.com'")
        print("  )")
        print()
        return 0
    else:
        print(f"✗ {total - passed}/{total} tests failed.")
        print()
        print("Troubleshooting:")
        print("1. Make sure you installed with: pip install -e .")
        print("2. Check you're in the correct virtual environment")
        print("3. Try reinstalling: pip uninstall gatewayz && pip install -e .")
        print()
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
