

import asyncio
from playwright.async_api import async_playwright

# ============================================================
# CONFIGURATION - Change this based on your operating system
# ============================================================
# Set to True for Mac, False for Windows
IS_MAC = False
# ============================================================

# Hard-coded topic list to skip dynamic scraping
HARD_CODED_TOPICS = [
    {"title": "C++ Basics", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cpp-foundation-cpp-basics-2"},
    {"title": "Variable and Data Types", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cpp-foundation-variables-and-data-types-2"},
    {"title": "Input Output in C++", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/foundation-cpp-io-in-cpp-2"},
    {"title": "Operators", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/foundation-cpp-operators-2"},
    {"title": "Flow Control", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/foundation-cpp-flow-control-2"},
    {"title": "Loops", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/foundation-cpp-loops-2"},
    {"title": "Function", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/foundation-cpp-function-2"},
    {"title": "Array", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/foundation-cpp-array-2"},
    {"title": "References", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/foundation-cpp-references"},
    {"title": "Pointers", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/foundation-cpp-pointers-2"},
    {"title": "String", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/foundation-cpp-string-2"},
    {"title": "Structure and Union", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/foundation-cpp-structure-union-2"},
    {"title": "Multi Dimensional Array", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/foundation-cpp-multidimension-2"},
    {"title": "Templates", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cpp-foundation-template-in-cpp-2"},
    {"title": "Object Oriented Programming (OOPs)", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/foundation-cpp-oops-2"},
    {"title": "Exception Handling", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/foundation-cpp-exception-handling"},
    {"title": "Advanced", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cpp-foundation-advanced-2"},
    {"title": "DSA - What, Why and How ?", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-intro-and-roadmap"},
    {"title": "Analysis of Algorithms", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-intro"},
    {"title": "Mathematics", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Mathematics"},
    {"title": "Bit Magic", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-BitMagic"},
    {"title": "Recursion", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Recursion"},
    {"title": "Arrays", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Arrays"},
    {"title": "Searching", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Searching"},
    {"title": "Sorting", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Sorting"},
    {"title": "Matrix", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Matrix"},
    {"title": "Hashing", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Hashing"},
    {"title": "Strings", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Strings"},
    {"title": "Linked List", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-LinkedList"},
    {"title": "Stack", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Stack"},
    {"title": "Queue", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Queue"},
    {"title": "Deque", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Deque"},
    {"title": "Tree", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Tree"},
    {"title": "Binary Search Tree", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-BST"},
    {"title": "Heap", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Heap"},
    {"title": "Graph", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Graph"},
    {"title": "Greedy", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Greedy"},
    {"title": "Backtracking", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Backtracking"},
    {"title": "Dynamic Programming", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-DP"},
    {"title": "Trie", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Trie"},
    {"title": "Segment and Binary Indexed Trees", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Segment-Tree"},
    {"title": "Disjoint Set", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-DisjointSet"},
    {"title": "N Queens Visualizer", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/n-queens-visualizer"},
    {"title": "Binary Tree Visualizer", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/binary-tree-visualizer"},
    {"title": "Sudoku Solver", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Project-Sudoku"},
    {"title": "Shortest Path Finder", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Project-Path-Finder"},
    {"title": "Tic Tac Toe", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/DSASP-Project-tic-tac-toe"},
    {"title": "Starting with CP", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/starting-with-cpcourse"},
    {"title": "Prefix Sum | Two Pointer | Sliding Window - Quick CP Revise and Problem Solving", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-prefix-sum"},
    {"title": "Number Theory Basics", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-number-basics"},
    {"title": "Basic Problem Practice", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-basic-problem-practice"},
    {"title": "Bit Masking", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-math-bitMasking"},
    {"title": "Fibonacci", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-maths-fibonacci"},
    {"title": "Divisors", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-math-divisors"},
    {"title": "Prime Factorization", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-math-primeFactorization"},
    {"title": "Prime Numbers", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-prime-number"},
    {"title": "GCD & LCM", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-maths-gcd"},
    {"title": "Mathematical Principles", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-math-mathematicalPrinciples"},
    {"title": "Number Theoretic Functions", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-math-numberTheoreticFunctions"},
    {"title": "Binomial Coefficients", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-math-binomialCoefficients"},
    {"title": "Catalan Numbers", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-maths-catalan-numbers"},
    {"title": "Modular Arithmetic", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-math-modularOperations"},
    {"title": "Modular Exponentiation", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-maths-modular-exponentiation"},
    {"title": "Combinatorial Game Theory", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-maths-combinatorial-game-theory"},
    {"title": "Geometric Algorithms", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-maths-geometric-algorithms"},
    {"title": "Miscellaneous Problems", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-miscellaneous"},
    {"title": "Recursion", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/recursion-cpcourse"},
    {"title": "Backtracking", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/backtracking-cpcourse"},
    {"title": "Binary Search", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/binary-search-cpcourse"},
    {"title": "Ternary Search", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/ternarysearch-cpcourse"},
    {"title": "Stack", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/stack-basic-cpcourse"},
    {"title": "Queue", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/queue-basic-cpcourse"},
    {"title": "Priority Queue", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/priority-queue-cpcourse"},
    {"title": "Traversals in Tree", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/tree-traversal"},
    {"title": "Extra Concepts and Problem Solving", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/more-cp-concept"},
    {"title": "Greedy", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/greedy-cpcourse"},
    {"title": "Walkthrough & BFS", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-bfs"},
    {"title": "DFS", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-dfs"},
    {"title": "Topological Sort", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-topological-sort"},
    {"title": "Lowest Common Ancestor", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-lowest-common-ancestor"},
    {"title": "Bridges and Articulation Point", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-bridges-and-articulation-point"},
    {"title": "Euler Path and Circuit", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-euler-path-and-circuit"},
    {"title": "Bipartite", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-bipartite"},
    {"title": "Disjoint Sets", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-disjoint-sets"},
    {"title": "Strongly connected components", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-strongly-connected-components"},
    {"title": "Shortest Path Algorithms", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cpcourse-single-graph"},
    {"title": "Graph- Spanning Trees", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/graph-spanning-trees"},
    {"title": "String", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/string-cpcourse"},
    {"title": "Standard DP Algorithms", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/standard-dp-cpcourse"},
    {"title": "2D DP", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-2d-dp"},
    {"title": "Combinatorics", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/combinatorics-dp-cpcourse"},
    {"title": "More Problem Solving", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/basic-dp-cpcourse"},
    {"title": "Range DP", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/rangedp-cpcourse"},
    {"title": "Bitmask DP", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/bitwisedp-cpcourse"},
    {"title": "Expected Value", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-expected-value"},
    {"title": "Probability DP", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-probability-dp"},
    {"title": "Digit DP", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-digit-dp"},
    {"title": "Sparse Table", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-sparse-table"},
    {"title": "Segment Tree", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-segment-tree"},
    {"title": "Merge Sort Tree", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-merge-sort-tree"},
    {"title": "Lazy Propagation", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-lazy-propagation"},
    {"title": "Fenwick Tree", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-fenwick-tree"},
    {"title": "Range Queries Problems", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-range-queries-problems"},
    {"title": "Number Theory", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-number-theory-interview"},
    {"title": "Recursion and Backtracking", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-recursion-backtracking-interview"},
    {"title": "Divide and Conquer", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-divide-conquer-interview"},
    {"title": "Stack and Queue", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-stack-queue-interview"},
    {"title": "Trees", "href": "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp/track/cp-trees-interview-questions"}
]


# OS-specific settings
if IS_MAC:
    CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    USER_AGENT = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
    PLATFORM = "MacIntel"
else:
    CHROME_PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
    PLATFORM = "Win32"

async def expand_all_sections(page):
    """Expand all category sections (weeks) on the Resources page"""
    print("[INFO] Expanding all week sections...")
    
    # Get all section headers (Week 1, Week 2, etc.)
    sections = await page.query_selector_all("div.batch_category_header___igBF")
    
    print(f"  Found {len(sections)} sections to expand")
    
    for i, section in enumerate(sections):
        try:
            # Check if section is already open (has batch_open__FkoHN class)
            parent = await section.evaluate_handle("el => el.closest('.batch_individual_tab__type___wbkY')")
            is_open = await parent.evaluate("el => el.classList.contains('batch_open__FkoHN')")
            
            if not is_open:
                await section.click()
                await asyncio.sleep(1)
                print(f"  [OK] Expanded section {i+1}")
            else:
                print(f"  [SKIP] Section {i+1} already open")
        except Exception as e:
            print(f"  [WARN] Could not expand section {i+1}: {e}")
    
    await asyncio.sleep(2)

async def get_topic_links(page):
    """Get all topic links from expanded sections, including sub-tabs"""
    await asyncio.sleep(2)
    
    all_topics = []
    seen = set()
    
    # First, find all main sections that are open
    sections = await page.query_selector_all("div.batch_individual_tab__type___wbkY.batch_open__FkoHN")
    print(f"[INFO] Found {len(sections)} open sections to process")
    
    for section_idx, section in enumerate(sections):
        try:
            # Check if this section has sub-tabs (like Basics, Number Theory I, etc.)
            sub_tabs = await section.query_selector_all("div.ui.pointing.secondary.menu a.item")
            
            if len(sub_tabs) > 0:
                print(f"  [INFO] Section {section_idx+1} has {len(sub_tabs)} sub-tabs")
                
                # Click each sub-tab and collect topics
                for tab_idx, tab in enumerate(sub_tabs):
                    tab_name = await tab.text_content()
                    print(f"    [TAB] Clicking sub-tab: {tab_name.strip()}")
                    
                    await tab.click()
                    await asyncio.sleep(1.5)
                    
                    # Now get topics from the active tab content
                    topic_links = await section.eval_on_selector_all(
                        "div.ui.segment.active.tab div.batch_items__RzVSg a[href*='/batch/'][href*='/track/']",
                        """elements => elements.map(el => {
                            const titleEl = el.querySelector('.batch_title__XImuz');
                            return {
                                href: el.href,
                                title: titleEl ? titleEl.textContent.trim() : 'Unknown'
                            };
                        })"""
                    )
                    
                    for topic in topic_links:
                        if topic['href'] not in seen:
                            seen.add(topic['href'])
                            all_topics.append(topic)
                            print(f"      Found: {topic['title']}")
            else:
                # No sub-tabs, just get topics directly
                topic_links = await section.eval_on_selector_all(
                    "div.batch_items__RzVSg a[href*='/batch/'][href*='/track/']",
                    """elements => elements.map(el => {
                        const titleEl = el.querySelector('.batch_title__XImuz');
                        return {
                            href: el.href,
                            title: titleEl ? titleEl.textContent.trim() : 'Unknown'
                        };
                    })"""
                )
                
                for topic in topic_links:
                    if topic['href'] not in seen:
                        seen.add(topic['href'])
                        all_topics.append(topic)
                        print(f"    Found: {topic['title']}")
                        
        except Exception as e:
            print(f"  [WARN] Error processing section {section_idx+1}: {e}")
    
    print(f"[INFO] Total unique topics found: {len(all_topics)}")
    return all_topics

async def click_videos_tab(page):
    """Click on the 'videos' tab in the sidebar to filter only videos"""
    try:
        # Try to find and click the videos tab
        # The videos tab has class sidebar_tabs__JmBlR and contains <p>videos</p>
        videos_tab = await page.query_selector("div.sidebar_tabs__JmBlR:has(p:text-is('videos'))")
        
        if videos_tab:
            # Check if already active
            class_attr = await videos_tab.get_attribute("class")
            if "active" not in (class_attr or ""):
                await videos_tab.click()
                print("  [TAB] Clicked on 'videos' tab")
                await asyncio.sleep(2)
            else:
                print("  [TAB] Videos tab already active")
            return True
        else:
            # Try alternative selector using xpath
            videos_tab = await page.query_selector("xpath=//div[contains(@class, 'sidebar_tabs__JmBlR')]//p[text()='videos']/..")
            if videos_tab:
                await videos_tab.click()
                print("  [TAB] Clicked on 'videos' tab (xpath)")
                await asyncio.sleep(2)
                return True
            else:
                print("  [WARN] Videos tab not found, will try to process all items")
                return False
    except Exception as e:
        print(f"  [WARN] Could not click videos tab: {e}")
        return False

async def get_sidebar_video_links(page):
    """Get all video links from the sidebar"""
    await asyncio.sleep(2)
    
    # Wait for sidebar to load
    try:
        await page.wait_for_selector("#scrollableContainer", timeout=10000)
    except:
        print("  [WARN] Sidebar not found")
        return []
    
    # Get all video links from sidebar
    video_links = await page.query_selector_all("#scrollableContainer a.sidebar_item__khyNp")
    return video_links

async def play_and_complete_video(page):
    """Play video, mute it, and wait for completion with periodic pause check"""
    try:
        # Wait for video player to load
        await asyncio.sleep(3)
        
        # Check if there's a video player
        video_player = await page.query_selector("div[id^='vjs_video_']")
        if not video_player:
            print("  [SKIP] No video player found (might be an article)")
            return True
        
        # Check if video is already completed (has vjs-ended class)
        is_already_ended = await page.evaluate('''
            () => {
                const player = document.querySelector('div[id^="vjs_video_"]');
                if (!player) return false;
                if (player.classList.contains('vjs-ended')) return true;
                const media = player.querySelector('video');
                if (!media || !media.duration || Number.isNaN(media.duration)) return false;
                return media.currentTime >= media.duration - 1; // treat near-end as done
            }
        ''')
        if is_already_ended:
            print("  [SKIP] Video already completed (at end)")
            return True
        
        # Helper: make controls visible and try to start playback
        async def wake_and_play():
            await page.evaluate('''() => {
                const player = document.querySelector('div[id^="vjs_video_"]');
                if (!player) return;
                player.classList.add('vjs-user-active');
                player.dispatchEvent(new Event('mousemove', { bubbles: true }));
                const controlBar = player.querySelector('.vjs-control-bar');
                if (controlBar) controlBar.style.opacity = '1';
                const playBtn = player.querySelector('button.vjs-play-control');
                if (playBtn) {
                    playBtn.style.display = 'block';
                    playBtn.style.opacity = '1';
                    playBtn.style.visibility = 'visible';
                    playBtn.style.pointerEvents = 'auto';
                }
            }''')
            play_control = page.locator("button.vjs-play-control")
            if await play_control.count() > 0:
                await play_control.scroll_into_view_if_needed()
                try:
                    await play_control.wait_for({"state": "visible", "timeout": 5000})
                except Exception:
                    pass
                for force_click in (False, True):
                    try:
                        await play_control.click(force=force_click, timeout=2000)
                        return True
                    except Exception:
                        continue
            big_play_locator = page.locator("button.vjs-big-play-button")
            if await big_play_locator.count() > 0:
                await big_play_locator.scroll_into_view_if_needed()
                try:
                    await big_play_locator.wait_for({"state": "visible", "timeout": 3000})
                except Exception:
                    pass
                for force_click in (False, True):
                    try:
                        await big_play_locator.click(force=force_click, timeout=2000)
                        return True
                    except Exception:
                        continue
            # XPath fallback for the big play button location provided
            xpath_play = page.locator("xpath=/html/body/div[1]/div/section[2]/section[2]/div[3]/div/div[1]/div/button")
            if await xpath_play.count() > 0:
                await xpath_play.scroll_into_view_if_needed()
                for force_click in (False, True):
                    try:
                        await xpath_play.click(force=force_click, timeout=2000)
                        return True
                    except Exception:
                        continue
            # Direct click on video surface using mouse (user-gesture emulation)
            video_surface = page.locator("video")
            if await video_surface.count() > 0:
                try:
                    box = await video_surface.bounding_box()
                    if box:
                        await page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
                        paused = await video_surface.evaluate("v => v.paused")
                        if not paused:
                            return True
                except Exception:
                    pass
            # JS fallback when buttons are hidden/overlayed
            clicked = await page.evaluate('''() => {
                const media = document.querySelector('video');
                if (!media) return false;
                media.muted = true;
                media.playsInline = true;
                if (media.currentTime >= media.duration - 1 && media.duration > 0) {
                    media.currentTime = 0; // restart if stuck at end
                }
                const btn = document.querySelector('button.vjs-play-control');
                if (btn) {
                    btn.style.display = 'block';
                    btn.style.visibility = 'visible';
                    btn.style.opacity = '1';
                    btn.style.pointerEvents = 'auto';
                    btn.click();
                }
                const playPromise = media.play();
                if (playPromise && typeof playPromise.catch === 'function') {
                    playPromise.catch(() => {
                        media.dispatchEvent(new Event('click', { bubbles: true }));
                    });
                }
                return true;
            }''')
            if clicked:
                try:
                    paused = await page.locator("video").evaluate("v => v.paused")
                    if not paused:
                        return True
                except Exception:
                    pass
            return False

        # Function to check if video is paused and resume it
        async def check_and_resume():
            is_paused = await page.evaluate('''
                () => {
                    const player = document.querySelector('div[id^="vjs_video_"]');
                    return player && player.classList.contains('vjs-paused');
                }
            ''')
            if is_paused:
                print("  [RESUME] Video was paused, resuming...")
                await wake_and_play()
                await asyncio.sleep(1)
        
        # Initial play - click play button
        started = await wake_and_play()
        if started:
            print("  [PLAY] Video started")
            await asyncio.sleep(2)
        
        # Also check if it's paused (for videos that were partially watched)
        await check_and_resume()
        
        # Mute the video
        mute_button = await page.query_selector("button.vjs-mute-control")
        if mute_button:
            await mute_button.click()
            print("  [MUTE] Video muted")
        
        # Wait for video to complete
        # Check every 5 seconds for completion, but only check pause every 60 seconds
        print("  [WAIT] Waiting for video to complete...")
        seconds_elapsed = 0
        while True:
            # Check if video ended or near-end
            is_ended = await page.evaluate('''
                () => {
                    const player = document.querySelector('div[id^="vjs_video_"]');
                    if (!player) return false;
                    if (player.classList.contains('vjs-ended')) return true;
                    const media = player.querySelector('video');
                    if (!media || !media.duration || Number.isNaN(media.duration)) return false;
                    return media.currentTime >= media.duration - 1;
                }
            ''')
            if is_ended:
                break
            
            # Check if paused every 60 seconds
            if seconds_elapsed % 60 == 0 and seconds_elapsed > 0:
                await check_and_resume()
            
            # Wait 5 seconds before next check
            await asyncio.sleep(5)
            seconds_elapsed += 5
        
        print("  [DONE] Video completed!")
        return True
        
    except Exception as e:
        print(f"  [ERROR] Error playing video: {e}")
        return False

async def process_all_videos_in_topic(page):
    """Process ALL videos in a topic using the sidebar"""
    
    # First, click on the "videos" tab to filter only videos
    await click_videos_tab(page)
    
    video_index = 0
    processed_urls = set()
    
    while True:
        sidebar_links = await get_sidebar_video_links(page)
        
        if not sidebar_links:
            print("  [WARN] No videos found in sidebar - skipping this topic")
            break
        
        total_videos = len(sidebar_links)
        print(f"\n  [INFO] Topic has {total_videos} videos total")
        
        found_next = False
        
        for idx, link in enumerate(sidebar_links):
            try:
                href = await link.get_attribute("href")
                class_attr = await link.get_attribute("class")
                is_active = "active" in (class_attr or "")
                
                parent_class = await link.evaluate("el => el.parentElement ? el.parentElement.className : ''")
                is_available = "progress_available" in parent_class
                
                if href in processed_urls and not is_active:
                    continue
                
                if is_active:
                    video_index = idx + 1
                    print(f"\n  [VIDEO] Playing video {video_index}/{total_videos}")
                    
                    success = await play_and_complete_video(page)
                    
                    if success:
                        processed_urls.add(href)
                        found_next = True
                        await asyncio.sleep(2)
                        
                        next_sidebar_links = await get_sidebar_video_links(page)
                        for next_idx, next_link in enumerate(next_sidebar_links):
                            next_href = await next_link.get_attribute("href")
                            if next_href not in processed_urls:
                                next_parent_class = await next_link.evaluate("el => el.parentElement ? el.parentElement.className : ''")
                                if "progress_available" in next_parent_class or next_href not in processed_urls:
                                    await next_link.click()
                                    print(f"  [NEXT] Moving to next video...")
                                    await asyncio.sleep(3)
                                    break
                        break
                    
                elif is_available and href not in processed_urls:
                    await link.click()
                    await asyncio.sleep(3)
                    
                    video_index = idx + 1
                    print(f"\n  [VIDEO] Playing video {video_index}/{total_videos}")
                    
                    success = await play_and_complete_video(page)
                    
                    if success:
                        processed_urls.add(href)
                        found_next = True
                        await asyncio.sleep(2)
                        break
                    
            except Exception as e:
                print(f"  [WARN] Error processing video: {e}")
                continue
        
        if not found_next:
            print(f"\n  [COMPLETE] All {total_videos} videos in this topic completed!")
            break
        
        await asyncio.sleep(1)

def get_starting_index(topics):
    """Allow user to select starting topic"""
    print(f"\n{'='*60}")
    print(f"Found {len(topics)} topics:")
    print(f"{'='*60}")
    
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic['title']}")
        print(f"   {topic['href']}")
    
    while True:
        try:
            start_input = input(f"\nEnter the starting topic number (1-{len(topics)}) [default: 1]: ").strip()
            
            if not start_input:
                return 0
                
            start_index = int(start_input) - 1
            
            if 0 <= start_index < len(topics):
                print(f"Starting from topic {start_index + 1}: {topics[start_index]['title']}")
                return start_index
            else:
                print(f"Please enter a number between 1 and {len(topics)}")
                
        except ValueError:
            print("Please enter a valid number")

async def main():
    async with async_playwright() as p:
        user_data_dir = "userdata"
        browser = await p.chromium.launch_persistent_context(
            user_data_dir,
            executable_path=CHROME_PATH,
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled"
            ],
            user_agent=USER_AGENT
        )

        page = await browser.new_page()
        
        await page.add_init_script(f"""
            Object.defineProperty(navigator, 'webdriver', {{get: () => undefined}});
            Object.defineProperty(navigator, 'platform', {{get: () => '{PLATFORM}'}});
            Object.defineProperty(navigator, 'vendor', {{get: () => 'Google Inc.'}});
            Object.defineProperty(navigator, 'language', {{get: () => 'en-US'}});
            Object.defineProperty(navigator, 'languages', {{get: () => ['en-US', 'en']}});
        """)
        
        # Go to main page first for login
        await page.goto("https://www.geeksforgeeks.org/")
        print("[INFO] Waiting 20 seconds for login...")
        await asyncio.sleep(3)

        # Navigate directly to Resources tab
        # Use predefined topic list instead of scraping
        topics = HARD_CODED_TOPICS
        print(f"[INFO] Loaded {len(topics)} hard-coded topics")

        # Let user choose starting point
        start_index = get_starting_index(topics)
        
        print(f"\n[START] Starting from topic {start_index + 1} out of {len(topics)} total topics")
        print("[INFO] Starting video automation...\n")

        # Process each topic
        for i, topic in enumerate(topics[start_index:], start=start_index + 1):
            print(f"\n{'='*60}")
            print(f"[TOPIC] {i}/{len(topics)}: {topic['title']}")
            print(f"   URL: {topic['href']}")
            print(f"{'='*60}")
            
            topic_url = topic['href']
            await page.goto(topic_url)
            await asyncio.sleep(3)
            
            # Process ALL videos in this topic using sidebar
            await process_all_videos_in_topic(page)
            
            print(f"\n[DONE] Completed topic {i}/{len(topics)}: {topic['title']}")
            await asyncio.sleep(2)

        print("\n[SUCCESS] All topics completed!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
