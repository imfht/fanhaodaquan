const fs = require("fs")
const path = require("path")
const ghcdn = require('github-to-cdn')

const profile = {
  username: "waifu-project",
  repo: "fanhaodaquan"
}

/**
 * 总数据
 */
const data = ghcdn({
  ...profile,
  path: "data/data.json"
})

/**
 * 车牌号
 */
const codes = ghcdn({
  ...profile,
  path: "data/codes.json"
})

const actress = ghcdn({
  ...profile,
  path: "data/actress.json"
})

const README_path = path.join(__dirname, "../README.md")

const README_txt = fs.readFileSync(README_path, "utf-8")

;(async ()=> {
  let sp = README_txt.split("\n")
  let ls = sp.filter(item=> {
    const flag = item == '<!-- ID -->'
    return !flag
  })
  let arr = [ data, codes, actress ]
  arr.forEach(item=> {
    ls.push(`- ${ item }`)
  })
  const result = ls.join('\n')
  console.log(result)
  // fs.writeFileSync(README_path, result)
})()

module.exports = {
  data,
  codes,
  actress,
  profile
}