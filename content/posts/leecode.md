---
title: "LeetCode 刷题记录"
date: 2025-03-18T09:46:23+08:00
draft: false
description: "LeetCode 算法题解与思路分析"
tags: ["LeetCode", "算法"]
categories: ["算法"]
author: "Heyuuuu"
---


### 小镇法官
##### 题干
小镇有 n 个人， 其中有一个人是是小镇法官。如果法官存在，那么：
1. 他不信任任何人
2. 每个人（除了他自己）都信任他
3. 同时满足 1 和 2

给定一个trust数组。其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人
如果小镇法官存在并确认身份，返回法官编号，否则返回 -1

##### 题解思路
如果使用图解的思路就很好接这个题目
![小镇法官](/images/judge.jpg)
引入两个概念就能很好的抽象这个题，对于小镇的某个人而言，别人信任我，表示入度，我信任别人表示出度。 因此，寻找小镇法官的题目可以抽象成， 法官的入度是 n-1，法官的出度是0.


##### code
```python3
from collections import Counter

def findJudge(n: int: trust: list(list(int, int))):
    outDegree = Counter([start for start, _ in trust])
    inDegree = Counter([end for _, end in trust])

    return next((i for i in range(0, n) if outDegree[i] == 0 and inDegree[i] == n-1), -1)
```


#### 1348.推文计数
##### 题目
一家社交媒体公司正试图通过分析特定时间段内出现的推文数量来监控其网站上的活动。这些时间段可以根据特定的频率（ 每分钟 、每小时 或 每一天 ）划分为更小的 时间段 。

例如，周期 [10,10000] （以 秒 为单位）将被划分为以下频率的 时间块 :

每 分钟 (60秒 块)： [10,69], [70,129], [130,189], ..., [9970,10000]
每 小时 (3600秒 块)：[10,3609], [3610,7209], [7210,10000]
每 天 (86400秒 块)： [10,10000]
注意，最后一个块可能比指定频率的块大小更短，并且总是以时间段的结束时间结束(在上面的示例中为 10000 )。

设计和实现一个API来帮助公司进行分析。

实现 TweetCounts 类:

TweetCounts() 初始化 TweetCounts 对象。
存储记录时间的 tweetName (以秒为单位)。
List<integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) 返回一个整数列表，表示给定时间 [startTime, endTime] （单位秒）和频率频率中，每个 时间块 中带有 tweetName 的 tweet 的数量。
freq 是 “minute” 、 “hour” 或 “day” 中的一个，分别表示 每分钟 、 每小时 或 每一天 的频率。






## 18. 4Sum(四数之和)
### 解题思路
#### 排序 + 双指针
本题是 15 题（三数之和）的扩展，核心思路是「降维」—— 通过两层循环固定前两个数，将四数之和转化为「两数之和」问题，再用双指针找后两个数，整体逻辑如下
1. 排序预处理
2. 固定第一个数
3. 固定第二个数
4. 双指针找出后两个数
5. 剪枝优化

```golang

package main

import (
    "fmt"
    "sort"
)

func fourSum(nums []int, target int) [][]int {
    var result [][]int
    n := len(nums)

    if n < 4 {
        return result
    }

    // step 1:
    sort.Ints(nums)

    // step 2:
    for i:=0; i<n-3; i++ {
        // 剪枝优化1, 跳过重复的第一个数
        if i > 0 && nums[i] == nums[i-1] {
            continue
        }

        // 剪枝优化， 如果最小的四个相加大于target，直接break
        if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target {
            break
        }

        // 剪枝优化， 如果当前最大的四个小于target，就跳过
        if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target {
            continue
        }

        // step3 固定第二个数
        for j := i+1; j < n-2; j++ {
            // 剪枝优化， 跳过重复的第二个数
            if j > i+1 && nums[j] == nums[j-1] {
                continue
            }

            // 剪枝2， 当前最小的超过target，break第二层循环
            if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target {
                break
            }

            // 剪枝3， 当前最大的不足target， 跳过循环
            if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target {
                continue
            }
            
            // step4, 双指针找到后两个数
            remain := target - nums[i] - nums[j]
            left, right := j+1, n-1
            for left < right {
                sum := nums[left] + nums[right]

                if sum == remain {
                    result = append(result, []int{nums[i], nums[j], nums[left], nums[right]})


                    for left < right && nums[left] == nums[left+1] {
                        left++
                    }

                    for left < right && nums[right] == nums[right-1] {
                        right--
                    }

                    left++
                    right--
                } else if sum < remain {
                    
                    left++
                } else {
                    right--
                }
            }
        }
    }

    return result
}

```