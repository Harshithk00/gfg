# GeeksforGeeks Video Automation

A Python script using Playwright to automatically play and complete videos from GeeksforGeeks batch courses.

## Features

- Automatically extracts all batch course links from a GeeksforGeeks batch page
- Allows user to select starting point (e.g., start from 6th link)
- Visits each batch link and plays all associated videos
- Waits for each video to complete before moving to the next one
- Uses persistent browser context to maintain login session
- Anti-detection measures to avoid automation blocking

## Prerequisites

- Python 3.7+
- Chrome browser installed
- GeeksforGeeks account with access to batch courses

## Installation

1. Install required dependencies:
```bash
pip install playwright
```

2. Install Playwright browsers:
```bash
playwright install chromium
```

## Usage

1. Run the script:
```python
python main.py
```

2. The script will:
   - Open Chrome browser
   - Navigate to GeeksforGeeks
   - Wait 10 seconds for you to manually login
   - Extract all batch links from the target course
   - Display numbered list of links and ask for starting point
   - Process videos from selected starting point

3. Select starting point:
```
Found 10 batch links:
1. https://www.geeksforgeeks.org/batch/...
2. https://www.geeksforgeeks.org/batch/...
...

Enter the starting link number (1-10) [default: 1]: 6
```

## Configuration

### Target Course
Change the `url` variable in `main()` function:
```python
url = "https://www.geeksforgeeks.org/batch/your-course-name?tab=Chapters"
```

### Chrome Path
Update the executable path if Chrome is installed in a different location:
```python
executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe"
```

### User Data Directory
The script creates a `userdata` folder to persist login sessions. You can change this:
```python
user_data_dir = "your_custom_folder"
```

## How It Works

1. **Login Session**: Uses persistent browser context to save login state
2. **Link Extraction**: Finds all links containing 'batch/' in href attribute
3. **Video Detection**: Looks for sidebar items with batch-related links
4. **Video Playback**: Clicks play button and monitors video player classes
5. **Completion Detection**: Waits for `vjs-ended` class to appear on video player
6. **Progress Tracking**: Shows current link and video progress

## Script Flow

```
1. Launch Chrome with persistent context
2. Navigate to GeeksforGeeks homepage
3. Wait for manual login (10 seconds)
4. Go to target batch course page
5. Extract all batch links
6. Display links and get user selection for starting point
7. For each selected link:
   - Navigate to batch page
   - Find all video links in sidebar
   - For each video:
     - Open in new tab
     - Click play button
     - Wait for video completion
     - Close tab
8. Close browser
```

## Troubleshooting

### Video Won't Play
- Ensure you're logged into GeeksforGeeks
- Check if the course requires payment/enrollment
- Verify the video player selector `#vjs_video_3` exists

### Script Stops Working
- GeeksforGeeks may have updated their HTML structure
- Update selectors in the script:
  - Video player: `#vjs_video_3`
  - Play button: `.vjs-big-play-button`
  - Sidebar items: `a[class*="sidebar_item"]`

### Chrome Path Issues
Update the Chrome executable path for your system:
- Windows: `C:/Program Files/Google/Chrome/Application/chrome.exe`
- Mac: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
- Linux: `/usr/bin/google-chrome`

## Important Notes

- This script is for educational purposes only
- Ensure you have proper access to the courses you're automating
- The script respects video completion requirements (watches full videos)
- Large courses may take significant time to complete
- Keep your computer active to prevent sleep mode interruption

## Customization

### Timeout Settings
Adjust wait times as needed:
```python
await asyncio.sleep(10)  # Wait between links
await asyncio.sleep(3)   # Wait after page load
```

### Selector Updates
If GeeksforGeeks updates their interface, update these selectors:
```python
# Batch links
"a[href*='batch/']"

# Video links  
'a[class*="sidebar_item"][href*="batch"]'

# Video player
'#vjs_video_3'

# Play button
'.vjs-big-play-button'
```

## License

This project is provided as-is for educational purposes. Use responsibly and in accordance with GeeksforGeeks terms of service.