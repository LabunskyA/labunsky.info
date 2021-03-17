# Introduction into the steganography data compression
This brief paper introduces a new class of compression techniques.

## The amount of information
The amount of information in a message is usually determined through the [information content](https://en.wikipedia.org/wiki/Information_content) as a simple bits count in its given representation. This definition is very important for scientific theory and other computer science, but not as intuitive while speaking about data compression. That's why I think we need some other way of defining it.

Information exists only in the perception of a being. Even if a [fallen tree](https://en.wikipedia.org/wiki/If_a_tree_falls_in_a_forest) makes a sound, it produces zero informational value. Such value should be consumed (stored, analyzed, modified, or transmitted) by someone or something to acquire a describable amount of information.

## Perceived information
Let `I(S\X)` represent the amount of information in `X` perceived by the subject `S`. By the subject, we can imply pretty much anything. The most straightforward examples are men (users) and digital media (like hard drives). Below they will be denoted as `U` and `M` accordingly. Generally, we can replace a human with any higher-level user without losing correctness, but this assumption delivers a more straightforward explanation.

The amount of information perceived by a human cannot be expressed with a number. Still, given two objects `X, Y` and user `U` we can compare `I(U\X)` and `I(U\Y)`. If `U` is saying that '`X` contains more information than `Y`' then `I(U\X) > I(U\Y)`.

Perceived information amount includes all of the information in `X` that `U` can interpret as an independent part. For example, if `X` is a JPEG photo and `U` is a man then `I(U\X)` includes both the visible amount in the image and all of the meta-, like a camera model, GPS coordinates or Huffman encoding table even if you need special separate tools to access them.

On the other hand, the amount of information perceived by the media may be easily (and most of the time - strictly) expressed by the number of bits in it. That's because it usually could be interpreted by the media in only one way possible - as some form of a binary sequence. Nor optical cables nor your hard drive could distinguish between graphics and audio content. That's because it was designed to pass interpretation jobs to a man or other higher-level users.

And since digital media provides us with strictly limited capabilities, there is a problem of reducing the amount of information perceived (stored/processed/etc.) by it without damage to the one perceived by the user. This is why we have different data compression techniques.

## Data compression techniques
By the process of compressing the data, I will imply presenting it in a way media perceives fewer bits than in the original. Such definition complies both with the traditional and these new terms. Traditionally, there are two main data compression techniques are considered: lossy and lossless ones.

Let `Y` be a result of some re-encoding of the message `X`. Utilizing the definition of the perceived amount of information, we can look at relations between the elements in `I(U\X), I(U\Y)` and `I(M\X), I(M\Y)` pairs. The only thing left to notice is that data compression requires `I(M\Y)` to be less or equal than `I(M\X)`. And that leaves us with only three possible relations left.

### If `I(U\X) = I(U\Y)` and `I(M\X) >~ I(M\Y)`
Then we are talking about lossless data compression. It is a special case of effective information encoding without altering a single bit of the one perceived by a user. The best example is a plain PNG image. It occupies way less space on the hard drive than plain pixel data.

### When `I(U\X) > I(U\Y)` and `I(M\X) >~ I(M\Y)`
And here we clearly can see lossy data compression. It utilizes human perception features for more efficient encoding with a possible loss of some 'unimportant parts. JPEG might be an example.

### The last one: `I(U\X) < I(U\Y)` and `I(M\X) >~ I(M\Y)`
Wait, what? This relation essentially describes the embedding process of additional information in `X` the way a user has access to it, but the media has no idea of existing.

To put it differently, this is a special use of **steganography methods** wherein the size of the 'container' `X` on a digital media is growing insignificantly or even compared to the amount of information stored in it without any kind of secrecy implied. You can hide data from your hard drive. Or whatever digital media you have in mind.
