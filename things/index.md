# Things I've made

Here is somewhat complete list of thins I made in my spare time. If you interested in any of it you can contact me via any method from the front page you like. You can also freely copy and distribute anything under BSD 3-clause (do whatever) license. Though I would be glad to be linked, just in case.

## A covert channel over (not only) the Telegram

We used to think of Telegram as a reliable and secure transmission medium for messages of any sort. But under the hood it has a rather common combination of a- and symmetric encryptions. Where’s fun in that? And why would anyone trust their private messages to the third-party anyway?

tl;dr - inventing a private covert channel through users blacklisting each other.

**More:** [medium/en](https://medium.com/@labunskya/secret-telegrams-bdd2035b6e84) [habr/ru](https://habr.com/ru/post/451954)

[GitHub](https://github.com/LabunskyA/covertele)

## A spy authentication protocol

So, we're sending super-secret under-cover agents Alice and Bob to a rival country. According to their mission they would need to contact and work with each other for some time, exchange some info - usual spies stuff. Of course, everything should be done with maximum possible security in mind.

After all, we don't want a disclosure - it threatens not only the agents themselves but the very national security. That's why it's our interest to provide them with minimal required information possible. In particular, less they knows about each other and communication methods - the better. But then how should agents authorize each other?

tl;dr - inventing authentication steganography-based technique for the imaginable three-letters agency.

**More:** [habr/ru](https://habr.com/ru/post/456670/)

[GitHub](https://github.com/LabunskyA/StegoAuth)


## Steganograpic proxy
You tired of VPN providers messing up with your data and having access to your personal info. Why not use something a bit more esoteric? Like, embedding your traffic into the images, videos or just some random plain text?

tl;dr - using simple steganographic channels as internet traffic proxies and a MitM prevention technique.

**More:** [habr/ru](https://habr.com/ru/post/319148/)

[GitHub](https://github.com/LabunskyA/StegoProxy)


## Introduction into steganographic data compression
tl;dr - describing data compression techniques based on steganography encoding missed in more classic disciplines.

**More:** [web/en](stego_compression), [web/ru](stego_compression/ru)

## About a strange data compression method
Another user tries to write a new data piece to his hard drive, but there is no space left. He refuses to delete anything since ‘he will need it later’. What should we do in this situation?

Such a problem is not a unique one. We have terabytes of data laying somewhere on our hard drives and it is not going to shrink any time soon. But how unique is it? All in all, every file is just a bit sequence, and it is probable that every new one is not all that different from the already stored ones.

Sure, you should not explicitly search for existing pieces of data on a hard drive — even if it is not a totally predictable failure, at least not a practical one. On the other hand, if the difference is not that great, maybe we can somehow fit one into the other…


tl;dr — trying to tell about strange data storage optimization technique using JPEG-files and F5 steganography algorithm.

**More:**  [medium/en](https://medium.com/@labunskya/about-a-strange-data-compression-method-4d0d9d2e5714), [habr/ru](https://habr.com/ru/post/453332/)

## f5ar

My implementation of the data compression technique described above. Written in pure C and compatible with pretty much any Unix-like platform, it will allow you to hide any of your data into jpeg photos and pictures without any noticeable loss in them while saving on total occupied hard drive space.

Works as intended, but completely useless nevertheless.

[GitHub](https://github.com/LabunskyA/f5ar)

## raw_ctype

While messing up with my own small NoSQL database written in C, I found out structure padding is wasting too much memory on a really big data sets. Using compiler-dependent tricks is never good enough for me as I want my code to be as portable as it is possible. 

That's why I played around with different compilers and found a way of partially neglecting structure padding using macros with zero performance impact. It is faster than using a typical `__packed__` directive and allows for more flexibility.

[GitHub](https://gist.github.com/LabunskyA/4ac8bcf10c70e7223fe4a8c0b201f897)

## getNya

A software parody for getting cute images written in a worst OOP design possible. Was first made as a satirical challenge: I would need to ask my teacher at the university to raise my grade 'cause I've written this thing. So I would need at the same time to violate any good patterns there are and make it look good enough for a lead java developer to be fooled by.

Now that's just a fun piece of software to mess around with.

[Website](http://labunskya.github.io/getNya/)
[GitHub](https://github.com/LabunskyA/getNya)

## Sabrina Online Reader

I like old-school web comics. And I like to read them as intended - through the web. Unfortunately, not every author has a good official online-reader available. So does this one. That's why I made my own from scratch using the same official data source. It is very simple, but also very usable. 

You can easily port it to any other web comic.

[Website](https://labunskya.github.io/SabrinaOnlineReader/)
[GitHub](https://github.com/LabunskyA/SabrinaOnlineReader)


## UsableVK

My everlasting battle with professional designers. Fixing social network design for them for a few years, making it better and more usable then the official one. Like, really, stop paying them. Their code is pure garbage most of the time with no consistency between revisions.

Almost always out of date due to my laziness.

[GitHub](https://github.com/LabunskyA/UsableVK)