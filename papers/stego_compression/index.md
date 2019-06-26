# Introduction into the data compression using steganography
This brief paper introduces a new class of compression techniques.

## The amount of information
The amount of information in a message usually determined through the [information content](https://en.wikipedia.org/wiki/Information_content) as basic bits count in a given representation.
This definition is very important for scientific theory and other computer science but not as intuitive when speaking about data compression.
That's why I think we need some other way of describing it.

Information exists only as a perception of a being.
Even if a [fallen tree](https://en.wikipedia.org/wiki/If_a_tree_falls_in_a_forest) makes a sound, it produces zero informational value.
So it should be consumed (stored, analyzed, modified or transmitted) by someone or something to acquire a describable amount of information.

## Perceived information
Let `I(S\X)` represent the amount of information in `X` perceived by the subject `S`.
By the subject, we can imply pretty much anything.
The most straightforward examples are men (users) and digital media.
Below they will be denoted as `U` and `M` accordingly.
Generally, we can replace a human with any higher-level user without losing correctness, but this assumption delivers a more straightforward explanation.

The amount of information perceived by a human cannot be expressed with numbers.
Still, given two objects `X, Y` and a user `U` we can compare `I(U\X)` and `I(U\Y)`.
If `U` is saying that '`X` contains more information than `Y`' then `I(U\X) > I(U\Y)`.

Perceived information amount includes all of the information in `X` that `U` can interpret as an independent part.
For example, if `X` is a JPEG photo and `U` is a man then `I(U\X)` includes both the visible amount in the image and all of the meta- one like a camera model, GPS coordinates or Huffman encoding table even if you need separate tools to access them.

On the other hand, the amount of information perceived by the media easily (and most of the time - strictly) expressed by the number of bits in it as was told before.
That's because it usually could be interpreted by the media in only one way possible - as a bit sequence.
Nor optical cables nor your hard drive could distinguish between graphics and audio content.
That's because it was designed to pass interpretation job to a man or some other kind of higher-level user.

And since digital media provides us with strictly limited capabilities, there is a problem of reducing the amount of information perceived (stored/processed/etc.) by the digital media without hurting the one perceived by a user.
This is why we have different data compression techniques.

## Data compression techniques
By a process of compressing data, I will imply representing it on a media in the way media perceives fewer bits than in the original.
This definition is compliant both with the traditional and our new terms.
There are traditionally two main data compression techniques considered: lossy and lossless ones.

Let `Y` be a result of some re-encoding of the `X`.
Utilizing the definition of the perceived amount of information, we can look at relations between the elements in `I(U\X), I(U\Y)` and `I(M\X), I(M\Y)` pairs.
The only thing left to notice is that data compression requires `I(M\Y)` to be less or equal than `I(M\X)` and that leaves us with only three possible relations left.

### If `I(U\X) = I(U\Y)` and `I(M\X) >~ I(M\Y)`
Then we are talking about lossless data compression.
It is basically a special case of an effective information encoding without altering a single bit of the one perceived by a user.

### When `I(U\X) > I(U\Y)` and `I(M\X) >~ I(M\Y)`
And here we clearly can see lossy data compression.
It utilizes human perception features for more efficient coding with a possible loss of some 'unimportant' parts.

### The last one: `I(U\X) < I(U\Y)` and `I(M\X) >~ I(M\Y)`
Wait, what?
This relation essentially describes the embedding of additional information in `X` the way a user has access to it, but not the media has no idea of existing.

To put it differently, this is a special use case of **steganography methods** wherein the size of the 'container' `X` on a digital media is growing insignificantly or even compared to the amount of information stored in it without any kind of secrecy implied.
In other words, you can actually hide data from your own hard drive.
Or whatever digital media you have in mind.

This article was written by Labunsky Artem and is distributed under the [Creative Commons BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) license.
You can distribute and use in any way you want until you are willing to give credit to the author and share the original work and any modifications under the same license.