## A spy authentication protocol
So, we're sending super-secret under-cover agents Alice and Bob to a rival country. According to their mission they would need to contact and work with each other for some time, exchange some info - usual spies stuff. Of course, everything should be done with maximum possible security in mind.

After all, we don't want a disclosure - it threatens not only the agents themselves but the very national security. That's why it's our interest to provide them with minimal required information possible. In particular, less they knows about each other and communication methods - the better. But then how should agents authorize each other?

TL;DR - inventing authentication steganography-based technique for the imaginable three-letters agency.

**Read more:**

- en: *in translation*
- ru: [habr](https://habr.com/ru/post/456670/)

  
## A covert channel over (not only) the Telegram
We used to think of Telegram as a reliable and secure transmission medium for messages of any sort. But under the hood it has a rather common combination of a- and symmetric encryptions. Where’s fun in that? And why would anyone trust their private messages to the third-party anyway?

TL;DR - inventing a private covert channel through users blacklisting each other.

**Read more:**

- en: [medium](https://medium.com/@labunskya/secret-telegrams-bdd2035b6e84)
- ru: [habr](https://habr.com/ru/post/451954)


## Steganograpic proxy
TL;DR - developing and testing steganographic channels capabilities as internet traffic proxies and a MitM prevention technique.

**Read more:** [habr](https://habr.com/ru/post/319148/)


## Introduction into steganographic data compression
TL;DR - describing data compression techniques based on steganography encoding missed in more classic disciplines.

**Read more:** 

- en: [html](compression), [markdown](compression/index.md)
- ru: *in translation*

  
## About a strange data compression method
Another user tries to write a new data piece to his hard drive, but there is no space left. He refuses to delete anything since ‘he will need it later’. What should we do in this situation?

Such a problem is not a unique one. We have terabytes of data laying somewhere on our hard drives and it is not going to shrink any time soon. But how unique is it? All in all, every file is just a bit sequence, and it is probable that every new one is not all that different from the already stored ones.

Sure, you should not explicitly search for existing pieces of data on a hard drive — even if it is not a totally predictable failure, at least not a practical one. On the other hand, if the difference is not that great, maybe we can somehow fit one into the other…


TL;DR — trying to tell about strange data storage optimization technique using JPEG-files and F5 steganography algorithm.

**Read more:**  

- en: [medium](https://medium.com/@labunskya/about-a-strange-data-compression-method-4d0d9d2e5714)
- ru: [habr](https://habr.com/ru/post/453332/)

