# Written by Arno Bakker
# see LICENSE for license information


def offset2piece(offset, piecesize, endpoint=True):
    p = offset / piecesize
    # Niels: 08-08-2011: included endpoint boolean to specify if we should return an inclusive piece
    if endpoint and offset % piecesize > 0:
        p += 1
    return p
