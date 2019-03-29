# On data compression techniques
This brief paper introduces a new fundamental compression technique.

## Perceived information
The amount of information in a message usually 

Let `I(S\X)` represent the amount of information in `X`, perceived by the subject `S`.
The subject can be pretty much anything.
The most straightforward examples are men (users) and digital media.
Below they will be denoted as `U` and `M` accordingly.

The amount of information perceived by humans cannot be expressed with numbers.
Still, given two information objects `X, Y` and a user `U` you can compare `I(U\X)` and `I(U\Y)`. If `U` is saying that '`X` contains more information than `Y`' then `I(U\X) > I(U\Y)`.

Perceived information implies all of the information in `X` that `U` can interpret as an independent piece.
For example, if `X` is a JPEG photo and `U` is a man then `I(U\X)` includes both the visible amount of information in the image and all of the meta- one like a camera model or GPS coordinates even if you need separate tools to access them.

On the other hand, the amount of information on the media easily expressed by the number of bits in it.
It usually interpreted in only only one way possible -  as a raw bit sequence on some kind of a file system. 
Furthermore, since they provide a strictly limited capacity, there is a problem of reducing the perceived amount of information by the digital media without hurting the one.
There is why we have different data compression techniques.

## Data compression techniques
By the process of compressing the information `X` I mean representing it in a way there are fewer bits required for the representation.
There are traditionally two main data compression techniques considered: lossy and lossless ones.

Let `Y` be a result of some re-coding of the `X`.
Utilizing the definition of the perceived amount of information, it is possible to describe them that ways:

### Lossless data compression
Is a special case of an effective information encoding without altering the one perceived by a user: `I(U\X) = I(U\Y)`, `I(M\X) > I(M\Y)`.

### Lossy data compression
Uses human perception features for more efficient coding with a possible loss of some 'unimportant' parts: `I(U\X) > I(U\Y)`, `I(M\X) > I(M\Y)`.

### Data compression using steganography
Worth noting that these two techniques do not describe every possible relation between `I(U\X), I(U\Y)` and `I(M\X), I(M\Y)` pairs.
There is only on relation left that makes sense from the data compression point of view: `I(U\X) < I(U\Y)`, `I(M\X) ~ I(M\Y)`. `~` means that perceived by the `M` amount of information is insignificantly different.

It essentially describes the embedding of additional information in `X` the way a user has access to it, but not a media by itself.
Put differently, this is a special use case of steganography methods wherein the size of the container `X` on a digital media is growing insignificantly compared to the amount of information stored in it without any kind of secrecy implied.
