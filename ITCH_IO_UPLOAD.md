# Complete Itch.io Upload Guide

## Prerequisites
- Pygbag installed: `pip install pygbag`
- Your game built and working locally

## Step-by-Step Upload Instructions

### 1. Build Your Web Version
Run this command in your game directory:

**Windows:**
```bash
build_web.bat
```

**Linux/Mac:**
```bash
bash build_web.sh
```

This creates a `dist/` folder with your web-playable game.

### 2. Create/Upload to Itch.io

#### A. Create a New Game (if you don't have one)
1. Go to [itch.io](https://itch.io) and log in
2. Click "Dashboard" → "Create new project"
3. Fill in the project details:
   - **Project Title**: DOOM-style Game
   - **Short Description**: A first-person raycasting game in the style of classic DOOM
   - **Kind of project**: Game
   - **Uploads**: (we'll do this next)

#### B. Upload the Game Files
1. On your project page, go to "Edit project"
2. Scroll to "Uploads"
3. Click "Upload files"
4. Select all files from the `dist/` folder (Ctrl+A inside the folder, then drag-and-drop)
5. **Important**: Check "This file will be played in the browser" ✓

#### C. Configure HTML Game Settings
1. After uploading, you'll see the file in the uploads list
2. Click the uploaded file to expand options
3. You should see **"Configure in the browser"** option - click it
4. Set these values:

   | Setting | Value |
   |---------|-------|
   | **Viewport Width** | 1300 |
   | **Viewport Height** | 720 |
   | **Frame Color** | #000000 |

   Or if you want a responsive game:
   | Setting | Value |
   |---------|-------|
   | **Viewport Width** | 100% |
   | **Viewport Height** | 100% |

5. Click "Save & continue"

### 3. Game Page Settings
1. Go to "Edit project"
2. Scroll to "Settings" 
3. Configure these important options:

   **Recommended Settings:**
   - **Embed in page**: ✓ Checked
   - **Fullscreen**: ✓ Checked  
   - **Can be played in the browser**: ✓ Checked
   - **Kind of project**: HTML
   - **Public**: ✓ Checked (or Restricted if you want)

### 4. Test Your Game
1. Go to your game page
2. Click "Run game" or refresh the page
3. Wait 30-60 seconds for the game to load (this is normal - WebAssembly takes time)
4. Test gameplay:
   - Mouse look (should work)
   - Keyboard controls
   - Weapon firing
   - NPC interactions

### 5. Troubleshooting Common Issues

#### Game Won't Load
- **Problem**: Blank white screen or "Loading..." stays forever
- **Solution**: 
  - Check browser console (F12 → Console tab) for errors
  - Make sure all files are in the dist folder
  - Try a different browser (Chrome is most reliable)
  - Increase timeout if needed

#### Performance Is Slow
- **Problem**: Game runs slowly or lags
- **Solution**:
  - This is normal for first 10-15 seconds (shader compilation)
  - Game should stabilize after that
  - Reduce window resolution if needed

#### Controls Don't Work
- **Problem**: Keyboard/Mouse not responding
- **Solution**:
  - Click on the game canvas first to give it focus
  - Check that mouse pointer lock is allowed (browser may ask)
  - In browser settings, allow "keyboard input" and "mouse movement"

#### Missing Graphics/Textures
- **Problem**: Game loads but sprites/textures are missing
- **Solution**:
  - Ensure all resource paths are relative (not absolute)
  - Check that resources/ folder is included in the build
  - Verify all image files are present in dist folder

### 6. Optional: Add More Information to Your Page

Add to your game's description:
```
DOOM-style Game - A first-person raycasting engine game

Controls:
- W/A/S/D - Move
- Mouse - Look around  
- Left Click - Shoot
- ESC - Exit game

Features:
- Raycasting 3D graphics
- NPCs with pathfinding AI
- Weapon system
- Dynamic lighting

Note: Game takes 30-60 seconds to load on first play (normal for web version).
```

### 7. Optional: Add Instructions

Create a "devlog" or pinned post with:
- Initial load time expectations
- Control scheme
- Known limitations
- Features

---

## Important Notes

✅ **What Works Great on Web:**
- Raycasting rendering (your game engine)
- Mouse look and keyboard controls
- Sprite rendering and object handling
- Sound and music (if properly configured)
- NPC AI and pathfinding

⚠️ **Potential Web Limitations:**
- First load is slower (30-60 seconds is normal)
- Performance varies by browser and system
- Some advanced features may need adjustment

✓ **Your Game is Perfect for Web Because:**
- It uses async/await (compatible with browser event loop)
- Pygame games work great with Pygbag
- Raycasting is efficient and web-friendly
- Resolution (1300x720) is ideal for browser

---

## Need More Help?

- **Pygbag Documentation**: https://github.com/pygame-web/pygbag
- **Itch.io HTML Games Guide**: https://itch.io/docs/creators/html5
- **Browser Issues**: Try Chrome, Firefox, or Safari
