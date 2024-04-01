import { extract } from '@extractus/article-extractor'



const input = 'https://www.livelaw.in/high-court/karnataka-high-court/karnataka-high-court-dangerous-dog-breeds-ban-stayed-252829'
// here we use top-level await, assume current platform supports it
try {
  const article = await extract(input)
  console.log(article)
} catch (err) {
  console.error(err)
}