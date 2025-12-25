---
title: "Stroop 效应打字游戏"
date: 2024-12-25T15:30:00+08:00
draft: false
description: "测试你的反应速度和注意力 - 经典 Stroop 效应游戏"
tags: ["游戏", "JavaScript", "认知心理学"]
---

挑战你的大脑！Stroop 效应是心理学中的经典现象，当颜色和文字不匹配时，你的反应会变慢。

<!--more-->

## 游戏说明

**三种模式：**
- 🟢 **简单模式**：颜色和文字一致，输入文字内容
- 🔴 **挑战模式**：颜色和文字不一致，输入显示的颜色（挑战你的注意力！）
- 🎲 **随机模式**：随机混合两种模式

**难度选择：**
- **普通**：4 种颜色
- **困难**：6 种颜色
- **极难**：8 种颜色

<style>
.stroop-container { max-width: 700px; margin: 30px auto; padding: 25px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.3); }
.stroop-content { background: white; border-radius: 15px; padding: 25px; }
.stroop-title { text-align: center; color: #667eea; font-size: 2em; margin-bottom: 20px; }
.mode-select, .difficulty-select { text-align: center; margin: 20px 0; }
.mode-btn, .difficulty-btn { padding: 12px 24px; margin: 5px; font-size: 1em; border: none; border-radius: 8px; cursor: pointer; transition: all 0.3s; font-weight: bold; }
.mode-btn { background: #e0e0e0; color: #333; }
.mode-btn.active { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(102,126,234,0.4); }
.difficulty-btn { background: #f0f0f0; color: #555; font-size: 0.9em; }
.difficulty-btn.active { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; }
.game-info { display: flex; justify-content: space-around; margin: 15px 0; padding: 15px; background: #f8f9fa; border-radius: 10px; }
.info-item { text-align: center; }
.info-label { color: #888; font-size: 0.85em; }
.info-value { font-weight: bold; color: #667eea; font-size: 1.3em; }
.game-area { text-align: center; padding: 50px 20px; background: #000; border-radius: 15px; margin: 20px 0; min-height: 180px; display: flex; flex-direction: column; justify-content: center; }
.mode-hint { color: #888; font-size: 0.9em; margin-bottom: 15px; }
.color-word { font-size: 3.5em; font-weight: bold; margin: 20px 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
.answer-input { width: 100%; max-width: 350px; padding: 15px; font-size: 1.2em; border: 3px solid #667eea; border-radius: 10px; text-align: center; outline: none; transition: all 0.3s; }
.answer-input:focus { border-color: #764ba2; box-shadow: 0 0 15px rgba(102,126,234,0.3); }
.feedback { margin-top: 15px; font-size: 1.2em; font-weight: bold; min-height: 30px; }
.feedback.correct { color: #28a745; }
.feedback.wrong { color: #dc3545; }
.control-btns { text-align: center; margin-top: 15px; }
.control-btn { padding: 10px 20px; margin: 5px; font-size: 0.95em; border: none; border-radius: 8px; cursor: pointer; background: #6c757d; color: white; transition: all 0.3s; }
.control-btn:hover { background: #5a6268; transform: translateY(-1px); }
.stats-modal { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.7); z-index: 1000; align-items: center; justify-content: center; }
.stats-modal.show { display: flex; }
.stats-content { background: white; padding: 30px; border-radius: 15px; max-width: 500px; width: 90%; }
.stats-title { text-align: center; color: #667eea; font-size: 1.8em; margin-bottom: 20px; }
.stats-table { width: 100%; margin: 20px 0; }
.stats-table td { padding: 12px; border-bottom: 1px solid #eee; }
.stats-table .label { text-align: right; color: #666; font-weight: bold; width: 50%; }
.stats-table .value { text-align: left; color: #667eea; font-size: 1.2em; font-weight: bold; }
.stats-comment { text-align: center; margin: 20px 0; padding: 15px; background: #f8f9fa; border-radius: 10px; font-size: 1.1em; font-weight: bold; }
.btn-restart { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 12px 30px; font-size: 1.1em; border: none; border-radius: 8px; cursor: pointer; transition: all 0.3s; }
.btn-restart:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(102,126,234,0.4); }
</style>

<div class="stroop-container">
<div class="stroop-content">
<h1 class="stroop-title">🎮 Stroop 效应游戏</h1>

<div class="mode-select">
<button class="mode-btn active" onclick="selectMode(1)" data-mode="1">😊 简单模式</button>
<button class="mode-btn" onclick="selectMode(2)" data-mode="2">🔥 挑战模式</button>
<button class="mode-btn" onclick="selectMode(3)" data-mode="3">🎲 随机模式</button>
</div>

<div class="difficulty-select">
<span style="color: #666; margin-right: 10px;">难度：</span>
<button class="difficulty-btn active" onclick="selectDifficulty('easy')" data-diff="easy">普通</button>
<button class="difficulty-btn" onclick="selectDifficulty('hard')" data-diff="hard">困难</button>
<button class="difficulty-btn" onclick="selectDifficulty('extreme')" data-diff="extreme">极难</button>
</div>

<div class="game-info">
<div class="info-item">
<div class="info-label">得分</div>
<div class="info-value"><span id="score">0</span>/<span id="total">0</span></div>
</div>
<div class="info-item">
<div class="info-label">准确率</div>
<div class="info-value"><span id="accuracy">0</span>%</div>
</div>
<div class="info-item">
<div class="info-label">连对</div>
<div class="info-value"><span id="streak">0</span></div>
</div>
</div>

<div class="game-area">
<div class="mode-hint" id="modeHint">输入文字内容（英文）</div>
<div class="color-word" id="colorWord">红色</div>
</div>

<div style="text-align: center;">
<input type="text" class="answer-input" id="answerInput" placeholder="输入答案后按 Enter" autocomplete="off">
<div class="feedback" id="feedback"></div>
</div>

<div class="control-btns">
<button class="control-btn" onclick="showStats()">查看统计</button>
<button class="control-btn" onclick="resetGame()">重新开始</button>
</div>
</div>
</div>

<div class="stats-modal" id="statsModal" onclick="hideStats(event)">
<div class="stats-content" onclick="event.stopPropagation()">
<h2 class="stats-title">📊 游戏统计</h2>
<table class="stats-table">
<tr><td class="label">总题数：</td><td class="value" id="finalTotal">0</td></tr>
<tr><td class="label">正确数：</td><td class="value" id="finalScore">0</td></tr>
<tr><td class="label">准确率：</td><td class="value" id="finalAccuracy">0%</td></tr>
<tr><td class="label">最高连对：</td><td class="value" id="maxStreak">0</td></tr>
<tr><td class="label">平均用时：</td><td class="value" id="avgTime">0s</td></tr>
</table>
<div class="stats-comment" id="comment"></div>
<div style="text-align: center;">
<button class="btn-restart" onclick="hideStats()">继续游戏</button>
</div>
</div>
</div>

<script>
const COLOR_SETS = {
  easy: {
    red: '红色', green: '绿色', blue: '蓝色', yellow: '黄色'
  },
  hard: {
    red: '红色', green: '绿色', blue: '蓝色', yellow: '黄色', magenta: '紫色', cyan: '青色'
  },
  extreme: {
    red: '红色', green: '绿色', blue: '蓝色', yellow: '黄色', 
    magenta: '紫色', cyan: '青色', orange: '橙色', purple: '紫罗兰'
  }
};

let gameState = {
  mode: 1,
  difficulty: 'easy',
  score: 0,
  total: 0,
  streak: 0,
  maxStreak: 0,
  startTime: null,
  roundStartTime: null,
  totalResponseTime: 0,
  currentAnswer: ''
};

function selectMode(mode) {
  gameState.mode = mode;
  document.querySelectorAll('.mode-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.mode == mode);
  });
  newQuestion();
}

function selectDifficulty(diff) {
  gameState.difficulty = diff;
  document.querySelectorAll('.difficulty-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.diff == diff);
  });
  newQuestion();
}

function newQuestion() {
  const colors = COLOR_SETS[gameState.difficulty];
  const colorKeys = Object.keys(colors);
  
  let mode = gameState.mode;
  if (mode === 3) mode = Math.random() < 0.5 ? 1 : 2;
  
  let colorKey, wordKey, hint;
  
  if (mode === 1) {
    colorKey = colorKeys[Math.floor(Math.random() * colorKeys.length)];
    wordKey = colorKey;
    hint = '输入文字内容（英文）';
    gameState.currentAnswer = colorKey;
  } else {
    colorKey = colorKeys[Math.floor(Math.random() * colorKeys.length)];
    const otherColors = colorKeys.filter(k => k !== colorKey);
    wordKey = otherColors[Math.floor(Math.random() * otherColors.length)];
    hint = '输入文字颜色（英文）';
    gameState.currentAnswer = colorKey;
  }
  
  document.getElementById('modeHint').textContent = hint;
  document.getElementById('colorWord').textContent = colors[wordKey];
  document.getElementById('colorWord').style.color = colorKey;
  document.getElementById('answerInput').value = '';
  document.getElementById('feedback').textContent = '';
  document.getElementById('feedback').className = 'feedback';
  
  gameState.roundStartTime = Date.now();
}

function checkAnswer() {
  const input = document.getElementById('answerInput');
  const userAnswer = input.value.trim().toLowerCase();
  
  if (!userAnswer) return;
  
  const responseTime = (Date.now() - gameState.roundStartTime) / 1000;
  gameState.totalResponseTime += responseTime;
  gameState.total++;
  
  const feedback = document.getElementById('feedback');
  const isCorrect = userAnswer === gameState.currentAnswer.toLowerCase();
  
  if (isCorrect) {
    gameState.score++;
    gameState.streak++;
    gameState.maxStreak = Math.max(gameState.maxStreak, gameState.streak);
    feedback.textContent = `✓ 正确！用时: ${responseTime.toFixed(2)}秒`;
    feedback.className = 'feedback correct';
  } else {
    gameState.streak = 0;
    feedback.textContent = `✗ 错误！正确答案: ${gameState.currentAnswer}`;
    feedback.className = 'feedback wrong';
  }
  
  updateStats();
  setTimeout(newQuestion, 1200);
}

function updateStats() {
  document.getElementById('score').textContent = gameState.score;
  document.getElementById('total').textContent = gameState.total;
  document.getElementById('streak').textContent = gameState.streak;
  
  const accuracy = gameState.total > 0 ? (gameState.score / gameState.total * 100).toFixed(1) : 0;
  document.getElementById('accuracy').textContent = accuracy;
}

function showStats() {
  document.getElementById('finalTotal').textContent = gameState.total;
  document.getElementById('finalScore').textContent = gameState.score;
  document.getElementById('maxStreak').textContent = gameState.maxStreak;
  
  const accuracy = gameState.total > 0 ? (gameState.score / gameState.total * 100).toFixed(1) : 0;
  document.getElementById('finalAccuracy').textContent = accuracy + '%';
  
  const avgTime = gameState.total > 0 ? (gameState.totalResponseTime / gameState.total).toFixed(2) : 0;
  document.getElementById('avgTime').textContent = avgTime + 's';
  
  let comment = '';
  if (accuracy >= 90) comment = '🏆 太棒了！你的反应速度惊人！';
  else if (accuracy >= 75) comment = '👍 很不错！继续保持！';
  else if (accuracy >= 60) comment = '💪 不错的表现，继续加油！';
  else comment = '😊 多练习就会进步！';
  
  document.getElementById('comment').textContent = comment;
  document.getElementById('statsModal').classList.add('show');
}

function hideStats(e) {
  if (!e || e.target.id === 'statsModal') {
    document.getElementById('statsModal').classList.remove('show');
  }
}

function resetGame() {
  gameState.score = 0;
  gameState.total = 0;
  gameState.streak = 0;
  gameState.maxStreak = 0;
  gameState.totalResponseTime = 0;
  updateStats();
  newQuestion();
}

document.getElementById('answerInput').addEventListener('keypress', function(e) {
  if (e.key === 'Enter') checkAnswer();
});

newQuestion();
</script>

