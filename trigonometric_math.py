import math

# Function to calculate the sine of a number in degrees
def cal_sin(num):
    radian = math.radians(num)  # Convert degrees to radians
    result = math.sin(radian)  # Calculate sine
    return result

# Function to calculate the cosine of a number in degrees
def cal_cos(num):
    radian = math.radians(num)  # Convert degrees to radians
    result = math.cos(radian)  # Calculate cosine
    return result

# Function to calculate the tangent of a number in degrees
def cal_tan(num):
    radian = math.radians(num)  # Convert degrees to radians
    result = math.tan(radian)  # Calculate tangent
    return result

# Function to calculate the arcsine of a number and return the result in degrees
def cal_asin(num):
    radian = math.asin(num)  # Calculate arcsine in radians
    result = math.degrees(radian)  # Convert radians to degrees
    return result

# Function to calculate the arccosine of a number and return the result in degrees
def cal_acos(num):
    radian = math.acos(num)  # Calculate arccosine in radians
    result = math.degrees(radian)  # Convert radians to degrees
    return result

# Function to calculate the arctangent of a number and return the result in degrees
def cal_atan(num):
    radian = math.atan(num)  # Calculate arctangent in radians
    result = math.degrees(radian)  # Convert radians to degrees
    return result