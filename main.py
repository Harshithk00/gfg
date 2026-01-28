# # # import asyncio
# # # from playwright.async_api import async_playwright

# # # async def get_batch_links(page):
# # #     # Get all hrefs where link contains 'batch/'
# # #     await asyncio.sleep(10)  # Wait for page to load
# # #     await page.wait_for_selector("a[href*='batch/']")
# # #     hrefs = await page.eval_on_selector_all(
# # #         "a[href*='batch/']",
# # #         "elements => elements.map(el => el.href)"
# # #     )
# # #     return hrefs

# # # async def visit_links(page, links, browser):
# # #     for i, link in enumerate(links):
# # #         print(f"🌐 Visiting link {i+1}/{len(links)}: {link}")
# # #         await page.goto(link)
        
# # #         # Get all href attributes
# # #         # Extract only batch-related links
# # #         await page.wait_for_selector('a[class*="sidebar_item"][href*="batch"]')
# # #         course_urls = await page.eval_on_selector_all('a[class*="sidebar_item"][href*="batch"]', 
# # #                         'elements => elements.map(element => element.href)'
# # #         )
        
# # #         print(len(course_urls))
        
# # #         if(course_urls):
# # #             for course_url in course_urls:
# # #                 print(f"🔗 Found course link: {course_url}")
# # #                 page2 = await browser.new_page()
# # #                 await page2.goto(course_url)
# # #                 await asyncio.sleep(3)
                
# # #                 await page2.click('.vjs-big-play-button')
                
# # #                 print("Waiting for video to complete...")
# # #                 await page2.wait_for_function('''
# # #                     () => {
# # #                         const videoPlayer = document.querySelector('#vjs_video_3');
# # #                         return videoPlayer && videoPlayer.classList.contains('vjs-ended');
# # #                         }
# # #                     ''', timeout=0)  # No timeout - wait indefinitely

# # #                 print("Video completed successfully!")
                
# # #                 await page2.close()  # Close page after visiting
                
# # #         # Wait a bit before next link
# # #         await asyncio.sleep(10)  # Wait a bit before next link

# # # async def main():
# # #     async with async_playwright() as p:
# # #         # Use persistent context (saves login session in "userdata" folder)
# # #         user_data_dir = "userdata"
# # #         browser = await p.chromium.launch_persistent_context(
# # #             user_data_dir,
# # #             executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe",
# # #             headless=False,
# # #             args=[
# # #                 "--disable-blink-features=AutomationControlled"  # Hide automation
# # #             ],
# # #             user_agent=(
# # #                 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
# # #                 "AppleWebKit/537.36 (KHTML, like Gecko) "
# # #                 "Chrome/139.0.0.0 Safari/537.36"
# # #             )
# # #         )

# # #         page = await browser.new_page()
        
        
# # #         await page.add_init_script("""
# # #             Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
# # #             Object.defineProperty(navigator, 'platform', {get: () => 'Win32'});
# # #             Object.defineProperty(navigator, 'vendor', {get: () => 'Google Inc.'});
# # #             Object.defineProperty(navigator, 'language', {get: () => 'en-US'});
# # #             Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
# # #         """)
        
# # #         # Go to main page
# # #         url = "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp?tab=Chapters"
# # #         await page.goto("https://www.geeksforgeeks.org/")

# # #         # Give 60 sec to login manually
# # #         print("⏳ Waiting 15 seconds for login...")
# # #         await asyncio.sleep(10)

# # #         # Navigate to target URL after login
# # #         await page.goto(url)
# # #         links = await get_batch_links(page)
# # #         print(f"✅ Found {len(links)} batch links")

# # #         # Visit them in sequence using same context
# # #         print("🌐 Visiting all batch links...")
# # #         await visit_links(page, links, browser)

# # #         await browser.close()

# # # if __name__ == "__main__":
# # #     asyncio.run(main())


# # import asyncio
# # from playwright.async_api import async_playwright

# # async def get_batch_links(page):
# #     # Get all hrefs where link contains 'batch/'
# #     await asyncio.sleep(10)  # Wait for page to load
# #     await page.wait_for_selector("a[href*='batch/']")
# #     hrefs = await page.eval_on_selector_all(
# #         "a[href*='batch/']",
# #         "elements => elements.map(el => el.href)"
# #     )
# #     return hrefs

# # def get_starting_index(links):
# #     """Allow user to select starting index"""
# #     print(f"\nFound {len(links)} batch links:")
# #     for i, link in enumerate(links):
# #         print(f"{i+1}. {link}")
    
# #     while True:
# #         try:
# #             start_input = input(f"\nEnter the starting link number (1-{len(links)}) [default: 1]: ").strip()
            
# #             if not start_input:  # Default to 1 if empty
# #                 return 0
                
# #             start_index = int(start_input) - 1  # Convert to 0-based index
            
# #             if 0 <= start_index < len(links):
# #                 print(f"Starting from link {start_index + 1}: {links[start_index]}")
# #                 return start_index
# #             else:
# #                 print(f"Please enter a number between 1 and {len(links)}")
                
# #         except ValueError:
# #             print("Please enter a valid number")

# # async def visit_links(page, links, browser, start_index=0):
# #     # Start from the selected index
# #     selected_links = links[start_index:]
# #     total_links = len(links)
    
# #     for i, link in enumerate(selected_links):
# #         current_position = start_index + i + 1
# #         print(f"🌐 Visiting link {current_position}/{total_links}: {link}")
# #         await page.goto(link)
        
# #         # Get all href attributes
# #         # Extract only batch-related links
# #         await page.wait_for_selector('a[class*="sidebar_item"][href*="batch"]')
# #         course_urls = await page.eval_on_selector_all('a[class*="sidebar_item"][href*="batch"]', 
# #                         'elements => elements.map(element => element.href)'
# #         )
        
# #         print(f"Found {len(course_urls)} course videos")
        
# #         if(course_urls):
# #             for j, course_url in enumerate(course_urls):
# #                 print(f"🔗 Processing video {j+1}/{len(course_urls)}: {course_url}")
# #                 page2 = await browser.new_page()
# #                 await page2.goto(course_url)
# #                 await asyncio.sleep(3)
                
# #                 await page2.click('.vjs-big-play-button')
                
# #                 print("Waiting for video to complete...")
# #                 await page2.wait_for_function('''
# #                     () => {
# #                         const videoPlayer = document.querySelector('#vjs_video_3');
# #                         return videoPlayer && videoPlayer.classList.contains('vjs-ended');
# #                         }
# #                     ''', timeout=0)  # No timeout - wait indefinitely

# #                 print("Video completed successfully!")
                
# #                 await page2.close()  # Close page after visiting
                
# #         # Wait a bit before next link
# #         await asyncio.sleep(10)  # Wait a bit before next link

# # async def main():
# #     async with async_playwright() as p:
# #         # Use persistent context (saves login session in "userdata" folder)
# #         user_data_dir = "userdata"
# #         browser = await p.chromium.launch_persistent_context(
# #             user_data_dir,
# #             executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe",
# #             headless=False,
# #             args=[
# #                 "--disable-blink-features=AutomationControlled"  # Hide automation
# #             ],
# #             user_agent=(
# #                 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
# #                 "AppleWebKit/537.36 (KHTML, like Gecko) "
# #                 "Chrome/139.0.0.0 Safari/537.36"
# #             )
# #         )

# #         page = await browser.new_page()
        
        
# #         await page.add_init_script("""
# #             Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
# #             Object.defineProperty(navigator, 'platform', {get: () => 'Win32'});
# #             Object.defineProperty(navigator, 'vendor', {get: () => 'Google Inc.'});
# #             Object.defineProperty(navigator, 'language', {get: () => 'en-US'});
# #             Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
# #         """)
        
# #         # Go to main page
# #         url = "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp?tab=Chapters"
# #         await page.goto("https://www.geeksforgeeks.org/")

# #         # Give 60 sec to login manually
# #         print("⏳ Waiting 15 seconds for login...")
# #         await asyncio.sleep(10)

# #         # Navigate to target URL after login
# #         await page.goto(url)
# #         links = await get_batch_links(page)
        
# #         # Let user choose starting point
# #         start_index = get_starting_index(links)
        
# #         print(f"✅ Starting from link {start_index + 1} out of {len(links)} total links")

# #         # Visit them in sequence using same context
# #         print("🌐 Starting video automation...")
# #         await visit_links(page, links, browser, start_index)

# #         await browser.close()


# import asyncio
# from playwright.async_api import async_playwright

# # ============================================================
# # CONFIGURATION - Change this based on your operating system
# # ============================================================
# # Set to True for Mac, False for Windows
# IS_MAC = True
# # ============================================================

# # OS-specific settings
# if IS_MAC:
#     CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
#     USER_AGENT = (
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
#         "AppleWebKit/537.36 (KHTML, like Gecko) "
#         "Chrome/120.0.0.0 Safari/537.36"
#     )
#     PLATFORM = "MacIntel"
# else:
#     CHROME_PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe"
#     USER_AGENT = (
#         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#         "AppleWebKit/537.36 (KHTML, like Gecko) "
#         "Chrome/120.0.0.0 Safari/537.36"
#     )
#     PLATFORM = "Win32"

# async def expand_all_sections(page):
#     """Expand all category sections (weeks) on the Resources page"""
#     print("[INFO] Expanding all week sections...")
    
#     # Get all section headers (Week 1, Week 2, etc.)
#     sections = await page.query_selector_all("div.batch_category_header___igBF")
    
#     print(f"  Found {len(sections)} sections to expand")
    
#     for i, section in enumerate(sections):
#         try:
#             # Check if section is already open (has batch_open__FkoHN class)
#             parent = await section.evaluate_handle("el => el.closest('.batch_individual_tab__type___wbkY')")
#             is_open = await parent.evaluate("el => el.classList.contains('batch_open__FkoHN')")
            
#             if not is_open:
#                 await section.click()
#                 await asyncio.sleep(1)
#                 print(f"  [OK] Expanded section {i+1}")
#             else:
#                 print(f"  [SKIP] Section {i+1} already open")
#         except Exception as e:
#             print(f"  [WARN] Could not expand section {i+1}: {e}")
    
#     await asyncio.sleep(2)

# async def get_topic_links(page):
#     """Get all topic links (Recursion, Arrays, etc.) from expanded week sections"""
#     await asyncio.sleep(2)
    
#     # Get topic links - these are inside batch_items__RzVSg divs
#     topic_links = await page.eval_on_selector_all(
#         "div.batch_items__RzVSg a[href*='/batch/'][href*='/track/']",
#         """elements => elements.map(el => {
#             const titleEl = el.querySelector('.batch_title__XImuz');
#             return {
#                 href: el.href,
#                 title: titleEl ? titleEl.textContent.trim() : 'Unknown'
#             };
#         })"""
#     )
    
#     # Remove duplicates while preserving order
#     seen = set()
#     unique_topics = []
#     for topic in topic_links:
#         if topic['href'] not in seen:
#             seen.add(topic['href'])
#             unique_topics.append(topic)
    
#     return unique_topics

# async def click_videos_tab(page):
#     """Click on the 'videos' tab in the sidebar to filter only videos"""
#     try:
#         # Try to find and click the videos tab
#         # The videos tab has class sidebar_tabs__JmBlR and contains <p>videos</p>
#         videos_tab = await page.query_selector("div.sidebar_tabs__JmBlR:has(p:text-is('videos'))")
        
#         if videos_tab:
#             # Check if already active
#             class_attr = await videos_tab.get_attribute("class")
#             if "active" not in (class_attr or ""):
#                 await videos_tab.click()
#                 print("  [TAB] Clicked on 'videos' tab")
#                 await asyncio.sleep(2)
#             else:
#                 print("  [TAB] Videos tab already active")
#             return True
#         else:
#             # Try alternative selector using xpath
#             videos_tab = await page.query_selector("xpath=//div[contains(@class, 'sidebar_tabs__JmBlR')]//p[text()='videos']/..")
#             if videos_tab:
#                 await videos_tab.click()
#                 print("  [TAB] Clicked on 'videos' tab (xpath)")
#                 await asyncio.sleep(2)
#                 return True
#             else:
#                 print("  [WARN] Videos tab not found, will try to process all items")
#                 return False
#     except Exception as e:
#         print(f"  [WARN] Could not click videos tab: {e}")
#         return False

# async def get_sidebar_video_links(page):
#     """Get all video links from the sidebar"""
#     await asyncio.sleep(2)
    
#     # Wait for sidebar to load
#     try:
#         await page.wait_for_selector("#scrollableContainer", timeout=10000)
#     except:
#         print("  [WARN] Sidebar not found")
#         return []
    
#     # Get all video links from sidebar
#     video_links = await page.query_selector_all("#scrollableContainer a.sidebar_item__khyNp")
#     return video_links

# async def play_and_complete_video(page):
#     """Play video, mute it, and wait for completion with periodic pause check"""
#     try:
#         # Wait for video player to load
#         await asyncio.sleep(3)
        
#         # Check if there's a video player
#         video_player = await page.query_selector("div[id^='vjs_video_']")
#         if not video_player:
#             print("  [SKIP] No video player found (might be an article)")
#             return True
        
#         # Check if video is already completed (has vjs-ended class)
#         is_already_ended = await page.evaluate('''
#             () => {
#                 const player = document.querySelector('div[id^="vjs_video_"]');
#                 return player && player.classList.contains('vjs-ended');
#             }
#         ''')
#         if is_already_ended:
#             print("  [SKIP] Video already completed")
#             return True
        
#         # Function to check if video is paused and resume it
#         async def check_and_resume():
#             is_paused = await page.evaluate('''
#                 () => {
#                     const player = document.querySelector('div[id^="vjs_video_"]');
#                     return player && player.classList.contains('vjs-paused');
#                 }
#             ''')
#             if is_paused:
#                 print("  [RESUME] Video was paused, resuming...")
#                 # Try clicking the play control button in the control bar
#                 play_control = await page.query_selector("button.vjs-play-control.vjs-paused")
#                 if play_control:
#                     await play_control.click()
#                 else:
#                     # Fallback: try the big play button
#                     big_play = await page.query_selector("button.vjs-big-play-button")
#                     if big_play:
#                         await big_play.click()
#                 await asyncio.sleep(1)
        
#         # Initial play - click play button
#         play_button = await page.query_selector("button.vjs-big-play-button")
#         if play_button:
#             await play_button.click()
#             print("  [PLAY] Video started")
#             await asyncio.sleep(2)
        
#         # Also check if it's paused (for videos that were partially watched)
#         await check_and_resume()
        
#         # Mute the video
#         mute_button = await page.query_selector("button.vjs-mute-control")
#         if mute_button:
#             await mute_button.click()
#             print("  [MUTE] Video muted")
        
#         # Wait for video to complete
#         # Check every 5 seconds for completion, but only check pause every 60 seconds
#         print("  [WAIT] Waiting for video to complete...")
#         seconds_elapsed = 0
#         while True:
#             # Check if video ended
#             is_ended = await page.evaluate('''
#                 () => {
#                     const player = document.querySelector('div[id^="vjs_video_"]');
#                     return player && player.classList.contains('vjs-ended');
#                 }
#             ''')
#             if is_ended:
#                 break
            
#             # Check if paused every 60 seconds
#             if seconds_elapsed % 60 == 0 and seconds_elapsed > 0:
#                 await check_and_resume()
            
#             # Wait 5 seconds before next check
#             await asyncio.sleep(5)
#             seconds_elapsed += 5
        
#         print("  [DONE] Video completed!")
#         return True
        
#     except Exception as e:
#         print(f"  [ERROR] Error playing video: {e}")
#         return False

# async def process_all_videos_in_topic(page):
#     """Process ALL videos in a topic using the sidebar"""
    
#     # First, click on the "videos" tab to filter only videos
#     await click_videos_tab(page)
    
#     video_index = 0
#     processed_urls = set()
    
#     while True:
#         sidebar_links = await get_sidebar_video_links(page)
        
#         if not sidebar_links:
#             print("  [WARN] No videos found in sidebar - skipping this topic")
#             break
        
#         total_videos = len(sidebar_links)
#         print(f"\n  [INFO] Topic has {total_videos} videos total")
        
#         found_next = False
        
#         for idx, link in enumerate(sidebar_links):
#             try:
#                 href = await link.get_attribute("href")
#                 class_attr = await link.get_attribute("class")
#                 is_active = "active" in (class_attr or "")
                
#                 parent_class = await link.evaluate("el => el.parentElement ? el.parentElement.className : ''")
#                 is_available = "progress_available" in parent_class
                
#                 if href in processed_urls and not is_active:
#                     continue
                
#                 if is_active:
#                     video_index = idx + 1
#                     print(f"\n  [VIDEO] Playing video {video_index}/{total_videos}")
                    
#                     success = await play_and_complete_video(page)
                    
#                     if success:
#                         processed_urls.add(href)
#                         found_next = True
#                         await asyncio.sleep(2)
                        
#                         next_sidebar_links = await get_sidebar_video_links(page)
#                         for next_idx, next_link in enumerate(next_sidebar_links):
#                             next_href = await next_link.get_attribute("href")
#                             if next_href not in processed_urls:
#                                 next_parent_class = await next_link.evaluate("el => el.parentElement ? el.parentElement.className : ''")
#                                 if "progress_available" in next_parent_class or next_href not in processed_urls:
#                                     await next_link.click()
#                                     print(f"  [NEXT] Moving to next video...")
#                                     await asyncio.sleep(3)
#                                     break
#                         break
                    
#                 elif is_available and href not in processed_urls:
#                     await link.click()
#                     await asyncio.sleep(3)
                    
#                     video_index = idx + 1
#                     print(f"\n  [VIDEO] Playing video {video_index}/{total_videos}")
                    
#                     success = await play_and_complete_video(page)
                    
#                     if success:
#                         processed_urls.add(href)
#                         found_next = True
#                         await asyncio.sleep(2)
#                         break
                    
#             except Exception as e:
#                 print(f"  [WARN] Error processing video: {e}")
#                 continue
        
#         if not found_next:
#             print(f"\n  [COMPLETE] All {total_videos} videos in this topic completed!")
#             break
        
#         await asyncio.sleep(1)

# def get_starting_index(topics):
#     """Allow user to select starting topic"""
#     print(f"\n{'='*60}")
#     print(f"Found {len(topics)} topics:")
#     print(f"{'='*60}")
    
#     for i, topic in enumerate(topics):
#         print(f"{i+1}. {topic['title']}")
#         print(f"   {topic['href']}")
    
#     while True:
#         try:
#             start_input = input(f"\nEnter the starting topic number (1-{len(topics)}) [default: 1]: ").strip()
            
#             if not start_input:
#                 return 0
                
#             start_index = int(start_input) - 1
            
#             if 0 <= start_index < len(topics):
#                 print(f"Starting from topic {start_index + 1}: {topics[start_index]['title']}")
#                 return start_index
#             else:
#                 print(f"Please enter a number between 1 and {len(topics)}")
                
#         except ValueError:
#             print("Please enter a valid number")

# async def main():
#     async with async_playwright() as p:
#         user_data_dir = "userdata"
#         browser = await p.chromium.launch_persistent_context(
#             user_data_dir,
#             executable_path=CHROME_PATH,
#             headless=False,
#             args=[
#                 "--disable-blink-features=AutomationControlled"
#             ],
#             user_agent=USER_AGENT
#         )

#         page = await browser.new_page()
        
#         await page.add_init_script(f"""
#             Object.defineProperty(navigator, 'webdriver', {{get: () => undefined}});
#             Object.defineProperty(navigator, 'platform', {{get: () => '{PLATFORM}'}});
#             Object.defineProperty(navigator, 'vendor', {{get: () => 'Google Inc.'}});
#             Object.defineProperty(navigator, 'language', {{get: () => 'en-US'}});
#             Object.defineProperty(navigator, 'languages', {{get: () => ['en-US', 'en']}});
#         """)
        
#         # Go to main page first for login
#         await page.goto("https://www.geeksforgeeks.org/")
#         print("[INFO] Waiting 20 seconds for login...")
#         await asyncio.sleep(20)

#         # Navigate directly to Resources tab
#         resources_url = "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp?tab=Resources"
#         print("[INFO] Navigating to Resources page...")
#         await page.goto(resources_url)
#         await asyncio.sleep(5)

#         # Expand all week sections
#         await expand_all_sections(page)

#         # Get all topic links from expanded sections
#         topics = await get_topic_links(page)
        
#         if not topics:
#             print("[ERROR] No topics found. Make sure you're logged in and sections are expanded.")
#             await browser.close()
#             return

#         # Let user choose starting point
#         start_index = get_starting_index(topics)
        
#         print(f"\n[START] Starting from topic {start_index + 1} out of {len(topics)} total topics")
#         print("[INFO] Starting video automation...\n")

#         # Process each topic
#         for i, topic in enumerate(topics[start_index:], start=start_index + 1):
#             print(f"\n{'='*60}")
#             print(f"[TOPIC] {i}/{len(topics)}: {topic['title']}")
#             print(f"   URL: {topic['href']}")
#             print(f"{'='*60}")
            
#             topic_url = topic['href']
#             await page.goto(topic_url)
#             await asyncio.sleep(3)
            
#             # Process ALL videos in this topic using sidebar
#             await process_all_videos_in_topic(page)
            
#             print(f"\n[DONE] Completed topic {i}/{len(topics)}: {topic['title']}")
#             await asyncio.sleep(2)

#         print("\n[SUCCESS] All topics completed!")
#         await browser.close()

# if __name__ == "__main__":
#     asyncio.run(main())

# # if __name__ == "__main__":
# #     asyncio.run(main())


import asyncio
from playwright.async_api import async_playwright

# ============================================================
# CONFIGURATION - Change this based on your operating system
# ============================================================
# Set to True for Mac, False for Windows
IS_MAC = True
# ============================================================

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
                return player && player.classList.contains('vjs-ended');
            }
        ''')
        if is_already_ended:
            print("  [SKIP] Video already completed")
            return True
        
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
                # Try clicking the play control button in the control bar
                play_control = await page.query_selector("button.vjs-play-control.vjs-paused")
                if play_control:
                    await play_control.click()
                else:
                    # Fallback: try the big play button
                    big_play = await page.query_selector("button.vjs-big-play-button")
                    if big_play:
                        await big_play.click()
                await asyncio.sleep(1)
        
        # Initial play - click play button
        play_button = await page.query_selector("button.vjs-big-play-button")
        if play_button:
            await play_button.click()
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
            # Check if video ended
            is_ended = await page.evaluate('''
                () => {
                    const player = document.querySelector('div[id^="vjs_video_"]');
                    return player && player.classList.contains('vjs-ended');
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
        await asyncio.sleep(20)

        # Navigate directly to Resources tab
        resources_url = "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp?tab=Resources"
        print("[INFO] Navigating to Resources page...")
        await page.goto(resources_url)
        await asyncio.sleep(5)

        # Expand all week sections
        await expand_all_sections(page)

        # Get all topic links from expanded sections
        topics = await get_topic_links(page)
        
        if not topics:
            print("[ERROR] No topics found. Make sure you're logged in and sections are expanded.")
            await browser.close()
            return

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
