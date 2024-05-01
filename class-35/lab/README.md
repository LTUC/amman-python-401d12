# Lab35 - React Review

- Today, you will create a react application (using functions components) that displays images and number of likes for each image. This application will allow you to like any image and to see the total number of likes for all images.

## Steps

Please follow the below steps as an example:

1. Create a new repo on Github called `401-images-app`.
2. Work on a `images` branch.
3. After completing the lab, create a PR from your `images` branch to `main` then merge your code.

## Lab Requirements

- Given the following array, use this data to display three `images` components:

```js
[{
    "_id": 1,
    "image_url": "https://i.pinimg.com/originals/a4/96/c2/a496c2b6bc5d7cfe0e0674f6598c38ad.jpg",
    "title": "nature1",
    "likes": 0
  },

  {
    "_id": 2,
    "image_url": "https://static.sadhguru.org/d/46272/1633199491-1633199490440.jpg",
    "title": "nature2",
    "likes": 0
  },

  {
    "_id": 3,
    "image_url": "https://wallpapercave.com/wp/u9AVLry.jpg",
    "title": "nature3",
    "likes": 0
}]
```

- Your application should display three cards. Each card should contain an image with its number of likes.
- Your application should allow the user to be able to interact with the images, so when the user clicks on an image, the number of likes for that image should be incremented by 1.
- Your application should display the total number of likes, which is a summation of all images likes.
- Each image should be displayed as independent component.
- All of images components should be displayed in the parent component.

## Submission Instructions

- Add the submission instructions