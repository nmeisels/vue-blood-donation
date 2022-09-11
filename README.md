# vue-blood-donation

[The website](https://nmeisels.github.io/vue-blood-donation/)

The official [Mada website](https://www.mdais.org/blood-donation) for blood drives does not let you filter by city or other parameters.
The site only lets you see the blood drive sites for a specific day.
This makes it complicated to find when the next blood drive is in a specific city. 
For these reasons I have developed this project that gives you a site with a grid and filter to see all of the blood drives.

I was inspired by [park_n_recs](https://github.com/NivRichter/park_n_recs) which was later integrated into the Israel Nature and Parks Authority website. If anyone has connections with Mada website please contact me :) 

# Backend
[FastAPI](https://fastapi.tiangolo.com/) server deployed using [deta](https://www.deta.sh/)

(I had issues with [cors](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) and this was my way of bypassing it)

# FrontEnd
Written in [Vue.js](https://vuejs.org/) using [ag-grid](https://www.ag-grid.com/)

# Disclaimer
This is a fun side project. I'm not a frontend developer. Any feedback how to improve the code is welcome!

# Sources
- [Vue.js Data Grid Getting Started With AG Grid](https://www.youtube.com/watch?v=V14w_NFuZB4&list=PLsZlhayVgqNz5iC0wFQDgixcAepFyrWbP&index=1&ab_channel=ag-Grid)
- [Deploy FastAPI on Deta](https://fastapi.tiangolo.com/deployment/deta/)
- [Deploying Vue Apps to Github Pages](https://medium.com/swlh/deploy-vue-app-to-github-pages-2ada48d7397e)

# Future ideas
- Telegram bot
- The ability to set reminders to donate with city preference etc.
- Push notification if you are close to a place with an ongoing blood drive
- More?
