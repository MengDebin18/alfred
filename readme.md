# Alfred
As this repo name shows, this is a collection of useful scripts combined into a single application, and written in favorite **python**. this will install into bin directory and standby at anytime when I want call it.
*alfred* mainly using for **Deep Learning** purpose.

![](https://i.loli.net/2018/02/05/5a77dd1e89e69.png)

![](https://i.loli.net/2018/02/05/5a77dd331bcb3.png)



Currently *alfred* contains several modules:

- vision:
  1. extract: combined command for extract images from videos;
  2. gray: covert a colorful image into gray image;
  3. 2video: combine an image sequence into a video;
  4. clean: clean all un-supported or broken image from a directory;
  5. faces: extract all faces from a single image or from a images dir;

- text:
  1. clean: clean a text file, which will clean all un-use words for nlp;
  2. translate: translate a words to target language;

- scrap:
  1. image: scrap images with a query words and save into local;

# Install
To install *alfred*, simply:

```
sudo python3 setup.py install
```
More powerful things is, you can import alfred in your project!

```
from alfred import vision
from alfred import text
```
So that you can access all alfred abilities in your own project!
