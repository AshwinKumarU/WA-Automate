from appium import webdriver

# Define desired capabilities
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "14",  # e.g., "11"
    "deviceName": "YOUR_DEVICE_NAME",          # e.g., "Pixel_4_Emulator" or the name shown by `adb devices`
    "automationName": "UiAutomator2",
    "appPackage": "com.whatsapp",
    "appActivity": "com.whatsapp.Main",
    "noReset": True  # Keeps the app's state between sessions
}

# Connect to the Appium server
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)
