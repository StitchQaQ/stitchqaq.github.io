#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stroop 效应打字游戏
两种模式：
1. 匹配模式 - 颜色和文字内容一致
2. 不匹配模式 - 颜色和文字内容不一致
"""

import random
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich import box

console = Console()

# 定义颜色和对应的中文名称
COLORS = {
    'red': '红色',
    'green': '绿色',
    'blue': '蓝色',
    'yellow': '黄色',
    'magenta': '紫色',
    'cyan': '青色',
}

COLOR_NAMES = list(COLORS.keys())
COLOR_CHINESE = list(COLORS.values())


class TypingGame:
    def __init__(self):
        self.score = 0
        self.total_rounds = 0
        self.start_time = None
        self.mode = None
    
    def show_welcome(self):
        """显示欢迎界面"""
        console.clear()
        welcome_text = """
[bold cyan]🎮 Stroop 效应打字游戏 🎮[/bold cyan]

[yellow]游戏规则：[/yellow]
看到彩色文字后，快速输入正确答案！

[bold green]模式 1 - 匹配模式：[/bold green]
颜色和文字内容一致
你需要输入：[bold]文字的内容[/bold]（英文，如 red）

[bold red]模式 2 - 不匹配模式（挑战）：[/bold red]
颜色和文字内容不一致
你需要输入：[bold]文字显示的颜色[/bold]（英文，而不是文字内容）

按 [bold]q[/bold] 退出游戏
        """
        console.print(Panel(welcome_text, box=box.DOUBLE, border_style="bright_blue"))
    
    def choose_mode(self):
        """选择游戏模式"""
        console.print("\n[bold]请选择游戏模式：[/bold]")
        console.print("[1] 匹配模式（简单）")
        console.print("[2] 不匹配模式（挑战）")
        console.print("[3] 随机模式（混合）")
        
        while True:
            choice = Prompt.ask("请输入", choices=["1", "2", "3", "q"])
            if choice == "q":
                return None
            self.mode = int(choice)
            return self.mode
    
    def generate_question(self, force_mode=None):
        """生成问题"""
        mode = force_mode if force_mode else self.mode
        
        if mode == 3:  # 随机模式
            mode = random.choice([1, 2])
        
        if mode == 1:  # 匹配模式
            color_key = random.choice(COLOR_NAMES)
            word = COLORS[color_key]
            correct_answer = color_key  # 英文答案
            hint = "输入文字内容（英文）"
        else:  # 不匹配模式
            color_key = random.choice(COLOR_NAMES)
            word_key = random.choice([k for k in COLOR_NAMES if k != color_key])
            word = COLORS[word_key]
            correct_answer = color_key  # 英文答案（文字显示的颜色）
            hint = "输入文字颜色（英文）"
        
        return color_key, word, correct_answer, hint, mode
    
    def play_round(self):
        """进行一轮游戏"""
        console.print("\n" + "=" * 50)
        color_key, word, correct_answer, hint, current_mode = self.generate_question()
        
        # 显示当前模式
        mode_text = "匹配模式" if current_mode == 1 else "不匹配模式"
        console.print(f"[dim]当前模式: {mode_text} | {hint}[/dim]")
        
        # 显示彩色文字
        console.print("\n")
        console.print(f"[bold {color_key}]{word}[/bold {color_key}]", justify="center", style="on black")
        console.print("\n")
        
        # 记录开始时间
        round_start = time.time()
        
        # 获取用户输入
        user_input = Prompt.ask("你的答案").strip().lower()
        
        if user_input == 'q':
            return False
        
        # 计算用时
        elapsed = time.time() - round_start
        
        # 检查答案（不区分大小写）
        if user_input == correct_answer.lower():
            self.score += 1
            console.print(f"[bold green]✓ 正确！[/bold green] 用时: {elapsed:.2f}秒", style="on black")
        else:
            console.print(f"[bold red]✗ 错误！[/bold red] 正确答案是: [bold]{correct_answer}[/bold]", style="on black")
        
        self.total_rounds += 1
        
        # 显示当前得分
        console.print(f"[dim]得分: {self.score}/{self.total_rounds}[/dim]")
        
        return True
    
    def show_stats(self):
        """显示统计信息"""
        if self.total_rounds == 0:
            return
        
        total_time = time.time() - self.start_time
        accuracy = (self.score / self.total_rounds) * 100
        avg_time = total_time / self.total_rounds
        
        console.print("\n")
        
        # 创建统计表格
        table = Table(title="[bold cyan]游戏统计[/bold cyan]", box=box.ROUNDED)
        table.add_column("项目", style="cyan", justify="right")
        table.add_column("数值", style="magenta", justify="left")
        
        table.add_row("总题数", str(self.total_rounds))
        table.add_row("正确数", str(self.score))
        table.add_row("准确率", f"{accuracy:.1f}%")
        table.add_row("总用时", f"{total_time:.1f}秒")
        table.add_row("平均用时", f"{avg_time:.2f}秒/题")
        
        console.print(table)
        
        # 评价
        if accuracy >= 90:
            console.print("\n[bold green]🏆 太棒了！你的反应速度惊人！[/bold green]")
        elif accuracy >= 70:
            console.print("\n[bold yellow]👍 不错！继续加油！[/bold yellow]")
        else:
            console.print("\n[bold blue]💪 多练习就会进步！[/bold blue]")
    
    def run(self):
        """运行游戏"""
        self.show_welcome()
        
        mode = self.choose_mode()
        if mode is None:
            console.print("[yellow]游戏已取消[/yellow]")
            return
        
        console.print("\n[bold green]游戏开始！[/bold green]")
        console.print("[dim]（随时输入 'q' 退出游戏）[/dim]")
        
        self.start_time = time.time()
        
        # 游戏主循环
        while True:
            if not self.play_round():
                break
            
            # 每5题显示一次统计
            if self.total_rounds % 5 == 0:
                console.print("\n[bold blue]--- 阶段统计 ---[/bold blue]")
                self.show_stats()
        
        # 显示最终统计
        console.print("\n[bold cyan]游戏结束！[/bold cyan]")
        self.show_stats()
        console.print("\n[bold]感谢游玩！👋[/bold]")


def main():
    """主函数"""
    try:
        game = TypingGame()
        game.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]游戏被中断[/yellow]")
    except Exception as e:
        console.print(f"\n[red]发生错误: {e}[/red]")


if __name__ == "__main__":
    main()

