# O(nlogn) - time
# O(1) - space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds = list(reversed(blueShirtSpeeds))
    return sum([max(item[0], item[1]) for item in zip(redShirtSpeeds, blueShirtSpeeds)])