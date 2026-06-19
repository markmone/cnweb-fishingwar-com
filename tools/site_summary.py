import json
from datetime import datetime
from typing import Dict, List, Optional

SITE_INVENTORY = {
    "site": {
        "name": "捕鱼大作战官方网站",
        "url": "https://cnweb-fishingwar.com",
        "description": "提供捕鱼大作战游戏资讯、活动公告与玩家社区服务。"
    },
    "meta": {
        "keywords": ["捕鱼大作战", "fishing war", "街机捕鱼", "休闲竞技"],
        "tags": ["游戏", "捕鱼", "街机", "休闲", "对战"],
        "language": "zh-CN",
        "last_updated": "2025-04-01"
    },
    "sections": [
        {
            "title": "游戏简介",
            "content": "捕鱼大作战是一款以海洋狩猎为主题的多人竞技游戏，玩家可使用多种武器捕获鱼类并获取积分。"
        },
        {
            "title": "特色玩法",
            "content": "支持单人闯关、多人对战、BOSS挑战等多种模式，并配有丰富的道具系统与排行榜机制。"
        },
        {
            "title": "活动公告",
            "content": "定期推出限时赛事、节日礼包与玩家回馈活动，详情请关注官网动态。"
        }
    ]
}


def extract_keywords(data: Dict) -> List[str]:
    """从站点数据中提取关键词列表"""
    raw = data.get("meta", {}).get("keywords", [])
    return [kw.strip() for kw in raw if kw.strip()]


def extract_tags(data: Dict) -> List[str]:
    """从站点数据中提取标签列表"""
    raw = data.get("meta", {}).get("tags", [])
    return [t.strip() for t in raw if t.strip()]


def extract_url(data: Dict) -> str:
    """提取站点URL"""
    return data.get("site", {}).get("url", "")


def extract_description(data: Dict) -> str:
    """提取站点简短说明"""
    return data.get("site", {}).get("description", "")


def extract_section_titles(data: Dict) -> List[str]:
    """提取所有板块标题"""
    sections = data.get("sections", [])
    return [s.get("title", "") for s in sections if s.get("title")]


def build_summary(data: Dict) -> str:
    """构建结构化摘要字符串"""
    url = extract_url(data)
    description = extract_description(data)
    keywords = extract_keywords(data)
    tags = extract_tags(data)
    section_titles = extract_section_titles(data)

    lines = []
    lines.append("=" * 50)
    lines.append("站点结构化摘要")
    lines.append("=" * 50)
    lines.append(f"URL: {url}")
    lines.append(f"描述: {description}")
    lines.append(f"关键词: {', '.join(keywords)}")
    lines.append(f"标签: {', '.join(tags)}")
    lines.append(f"板块: {' | '.join(section_titles)}")
    lines.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-" * 50)
    return "\n".join(lines)


def generate_json_summary(data: Dict) -> str:
    """以JSON格式输出摘要（便于程序读取）"""
    summary = {
        "url": extract_url(data),
        "description": extract_description(data),
        "keywords": extract_keywords(data),
        "tags": extract_tags(data),
        "section_titles": extract_section_titles(data),
        "generated_at": datetime.now().isoformat()
    }
    return json.dumps(summary, ensure_ascii=False, indent=2)


def print_summary(data: Optional[Dict] = None) -> None:
    """打印站点摘要到控制台"""
    if data is None:
        data = SITE_INVENTORY
    print(build_summary(data))
    print()
    print("JSON 格式摘要:")
    print(generate_json_summary(data))


def build_custom_summary(
    url: str,
    description: str,
    keywords: List[str],
    tags: List[str],
    sections: List[str]
) -> str:
    """通过参数自定义生成摘要"""
    dummy_data = {
        "site": {"url": url, "description": description},
        "meta": {"keywords": keywords, "tags": tags},
        "sections": [{"title": t, "content": ""} for t in sections]
    }
    return build_summary(dummy_data)


def demo() -> None:
    """演示函数：展示默认摘要与自定义摘要"""
    print("=== 默认站点摘要 ===")
    print_summary()

    print("\n=== 自定义摘要示例 ===")
    custom = build_custom_summary(
        url="https://cnweb-fishingwar.com",
        description="捕鱼大作战官方站点",
        keywords=["捕鱼大作战", "街机", "对战"],
        tags=["游戏", "捕鱼"],
        sections=["主页", "新闻", "排行榜"]
    )
    print(custom)


if __name__ == "__main__":
    demo()