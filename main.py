# import asyncio
# from playwright.async_api import async_playwright

# async def get_batch_links(page):
#     # Get all hrefs where link contains 'batch/'
#     await asyncio.sleep(10)  # Wait for page to load
#     await page.wait_for_selector("a[href*='batch/']")
#     hrefs = await page.eval_on_selector_all(
#         "a[href*='batch/']",
#         "elements => elements.map(el => el.href)"
#     )
#     return hrefs

# async def visit_links(page, links, browser):
#     for i, link in enumerate(links):
#         print(f"🌐 Visiting link {i+1}/{len(links)}: {link}")
#         await page.goto(link)
        
#         # Get all href attributes
#         # Extract only batch-related links
#         await page.wait_for_selector('a[class*="sidebar_item"][href*="batch"]')
#         course_urls = await page.eval_on_selector_all('a[class*="sidebar_item"][href*="batch"]', 
#                         'elements => elements.map(element => element.href)'
#         )
        
#         print(len(course_urls))
        
#         if(course_urls):
#             for course_url in course_urls:
#                 print(f"🔗 Found course link: {course_url}")
#                 page2 = await browser.new_page()
#                 await page2.goto(course_url)
#                 await asyncio.sleep(3)
                
#                 await page2.click('.vjs-big-play-button')
                
#                 print("Waiting for video to complete...")
#                 await page2.wait_for_function('''
#                     () => {
#                         const videoPlayer = document.querySelector('#vjs_video_3');
#                         return videoPlayer && videoPlayer.classList.contains('vjs-ended');
#                         }
#                     ''', timeout=0)  # No timeout - wait indefinitely

#                 print("Video completed successfully!")
                
#                 await page2.close()  # Close page after visiting
                
#         # Wait a bit before next link
#         await asyncio.sleep(10)  # Wait a bit before next link

# async def main():
#     async with async_playwright() as p:
#         # Use persistent context (saves login session in "userdata" folder)
#         user_data_dir = "userdata"
#         browser = await p.chromium.launch_persistent_context(
#             user_data_dir,
#             executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe",
#             headless=False,
#             args=[
#                 "--disable-blink-features=AutomationControlled"  # Hide automation
#             ],
#             user_agent=(
#                 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                 "AppleWebKit/537.36 (KHTML, like Gecko) "
#                 "Chrome/139.0.0.0 Safari/537.36"
#             )
#         )

#         page = await browser.new_page()
        
        
#         await page.add_init_script("""
#             Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
#             Object.defineProperty(navigator, 'platform', {get: () => 'Win32'});
#             Object.defineProperty(navigator, 'vendor', {get: () => 'Google Inc.'});
#             Object.defineProperty(navigator, 'language', {get: () => 'en-US'});
#             Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
#         """)
        
#         # Go to main page
#         url = "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp?tab=Chapters"
#         await page.goto("https://www.geeksforgeeks.org/")

#         # Give 60 sec to login manually
#         print("⏳ Waiting 15 seconds for login...")
#         await asyncio.sleep(10)

#         # Navigate to target URL after login
#         await page.goto(url)
#         links = await get_batch_links(page)
#         print(f"✅ Found {len(links)} batch links")

#         # Visit them in sequence using same context
#         print("🌐 Visiting all batch links...")
#         await visit_links(page, links, browser)

#         await browser.close()

# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
from playwright.async_api import async_playwright

async def get_batch_links(page):
    # Get all hrefs where link contains 'batch/'
    await asyncio.sleep(10)  # Wait for page to load
    await page.wait_for_selector("a[href*='batch/']")
    hrefs = await page.eval_on_selector_all(
        "a[href*='batch/']",
        "elements => elements.map(el => el.href)"
    )
    return hrefs

def get_starting_index(links):
    """Allow user to select starting index"""
    print(f"\nFound {len(links)} batch links:")
    for i, link in enumerate(links):
        print(f"{i+1}. {link}")
    
    while True:
        try:
            start_input = input(f"\nEnter the starting link number (1-{len(links)}) [default: 1]: ").strip()
            
            if not start_input:  # Default to 1 if empty
                return 0
                
            start_index = int(start_input) - 1  # Convert to 0-based index
            
            if 0 <= start_index < len(links):
                print(f"Starting from link {start_index + 1}: {links[start_index]}")
                return start_index
            else:
                print(f"Please enter a number between 1 and {len(links)}")
                
        except ValueError:
            print("Please enter a valid number")

async def visit_links(page, links, browser, start_index=0):
    # Start from the selected index
    selected_links = links[start_index:]
    total_links = len(links)
    
    for i, link in enumerate(selected_links):
        current_position = start_index + i + 1
        print(f"🌐 Visiting link {current_position}/{total_links}: {link}")
        await page.goto(link)
        
        # Get all href attributes
        # Extract only batch-related links
        await page.wait_for_selector('a[class*="sidebar_item"][href*="batch"]')
        course_urls = await page.eval_on_selector_all('a[class*="sidebar_item"][href*="batch"]', 
                        'elements => elements.map(element => element.href)'
        )
        
        print(f"Found {len(course_urls)} course videos")
        
        if(course_urls):
            for j, course_url in enumerate(course_urls):
                print(f"🔗 Processing video {j+1}/{len(course_urls)}: {course_url}")
                page2 = await browser.new_page()
                await page2.goto(course_url)
                await asyncio.sleep(3)
                
                await page2.click('.vjs-big-play-button')
                
                print("Waiting for video to complete...")
                await page2.wait_for_function('''
                    () => {
                        const videoPlayer = document.querySelector('#vjs_video_3');
                        return videoPlayer && videoPlayer.classList.contains('vjs-ended');
                        }
                    ''', timeout=0)  # No timeout - wait indefinitely

                print("Video completed successfully!")
                
                await page2.close()  # Close page after visiting
                
        # Wait a bit before next link
        await asyncio.sleep(10)  # Wait a bit before next link

async def main():
    async with async_playwright() as p:
        # Use persistent context (saves login session in "userdata" folder)
        user_data_dir = "userdata"
        browser = await p.chromium.launch_persistent_context(
            user_data_dir,
            executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe",
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled"  # Hide automation
            ],
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/139.0.0.0 Safari/537.36"
            )
        )

        page = await browser.new_page()
        
        
        await page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            Object.defineProperty(navigator, 'platform', {get: () => 'Win32'});
            Object.defineProperty(navigator, 'vendor', {get: () => 'Google Inc.'});
            Object.defineProperty(navigator, 'language', {get: () => 'en-US'});
            Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
        """)
        
        # Go to main page
        url = "https://www.geeksforgeeks.org/batch/dsa-siddaganga-2025-it-ccp?tab=Chapters"
        await page.goto("https://www.geeksforgeeks.org/")

        # Give 60 sec to login manually
        print("⏳ Waiting 15 seconds for login...")
        await asyncio.sleep(10)

        # Navigate to target URL after login
        await page.goto(url)
        links = await get_batch_links(page)
        
        # Let user choose starting point
        start_index = get_starting_index(links)
        
        print(f"✅ Starting from link {start_index + 1} out of {len(links)} total links")

        # Visit them in sequence using same context
        print("🌐 Starting video automation...")
        await visit_links(page, links, browser, start_index)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())