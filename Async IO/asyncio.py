import time
import asyncio
import requests


async def function1():
    print("Func 1")
    URL = "https://www.heroscreen.cc/2023/07/anime-wallpaper-4k-goku-vs-naruto.html"
    response = requests.get(URL)
    open("myimage.jpeg","wb").write(response.content)

    return "Akhilesh"

async def function2():
    print("func 2") 
    URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram2.jpg", "wb").write(response.content)
  
async def function3():
    print("func 3")
    URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)

async def main():
    # await function1()
    # await function2()
    # await function3()
    # return 3

    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)


    # task = asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()

asyncio.run(main())
