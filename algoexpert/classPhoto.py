# O(nlogn) - time
# O(1) - space

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    for idx in range(len(redShirtHeights)):
        if idx == 0:
            if redShirtHeights[idx] > blueShirtHeights[idx]:
                backrow = "red"
            elif redShirtHeights[idx] < blueShirtHeights[idx]:
                backrow = "blue"
            else:
                return False
        else:
            if redShirtHeights[idx] < blueShirtHeights[idx] and backrow == "red":
                return False
            elif redShirtHeights[idx] > blueShirtHeights[idx] and backrow == "blue":
                return False

    return True
