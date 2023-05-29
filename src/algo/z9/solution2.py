"""
Semantic versioning
https://devopedia.org/images/article/279/7179.1593248779.png

{Major}.{Minor}.{Patch}

np.

'1.3.6' oznacza major=1, minor=3, path=6


"""


def get_latest(versions: list[str]) -> str:
    """
    :return: Latest semantic version from the given `versions`
    """
    # todo: your code
    items = []
    items_int = []
    items_sorted = []
    result = []
    for item in versions:
        items.append( item.split("." ))
    for item1 in items :
        item1 = list(map(int, item1 ) )
        items_int.append(item1)
    items_sorted = sorted(items_int)
    for elem in items_sorted:
        x = '.'.join(str(y) for y in elem )
        result.append(x)
    return result[-1]
def next_version(version: str, level: int) -> str:
    """
    :param version: Current version
    :param level: Which part should be incremented; 0: major, 1: minor, 2: patch
    :return: Properly incremented version
    """
    # todo: your code
    items = []
    a = version.split(".")
    b = ([int(x) for x in a])
    if(level == 0):
        b[0] = b[0] + 1
        b[1] = 0
        b[2] = 0
    elif(level == 1):
        b[1]=b[1] + 1
        b[2]=0
    elif (level == 2) :
        b[2]=b[2] + 1
    result = ('.'.join(str(x) for x in b))
    return result