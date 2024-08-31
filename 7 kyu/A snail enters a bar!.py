"""
Problem Description:

A snail is crawling along a rubber band that has an initial length of x units. The snail moves at a constant speed of y units per minute. As the snail crawls from the left end of the rubber band to the right end, the rubber band increases in length from the right side every minute, adding z units to its length.

The question is: Will the snail be able to reach the right end of the rubber band within 1 year?

Parameters:

x: Initial length of the rubber band (in units), where 0.01 ≤ x ≤ 1,000,000.
y: Speed of the snail (in units per minute), where 0.01 ≤ y ≤ 1,000,000.
z: Amount by which the rubber band increases in length every minute (in units), where 0.01 ≤ z ≤ 1,000,000.
"""
def will_snail_reach_end(x, y, z):
    minutes_in_year = 60 * 24 * 365
    snail_position = 0.0
    rubber_band_length = x
    
    for minute in range(1, minutes_in_year + 1):
        snail_position += y / rubber_band_length
        
        if snail_position >= 1.0:
            return True

        rubber_band_length += z
        
    return False

# Example Usage
print(will_snail_reach_end(10, 2, 1))         # Expected output: True
print(will_snail_reach_end(100, 1, 2))        # Expected output: False
print(will_snail_reach_end(100000, 0.1, 0.05)) # Expected output: False