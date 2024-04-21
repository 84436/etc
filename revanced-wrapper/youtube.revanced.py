#!/usr/bin/env python3

APP_NAME = 'youtube'
APP_DISPLAY_NAME = 'YouTube'
TARGET_VERSION = '19.04.37'
PATCHES = [
    "Alternative thumbnails", # Adds options to replace video thumbnails using the DeArrow API or image captures from the video.
    "Bypass URL redirects", # Adds an option to bypass URL redirects and open the original URL directly.
    "Change start page", # Adds an option to set which page the app opens in instead of the homepage.
    "Client spoof", # Adds options to spoof the client to allow video playback.
    "Disable fullscreen ambient mode", # Adds an option to disable the ambient mode when in fullscreen.
    "Disable player popup panels", # Adds an option to disable panels (such as live chat) from opening automatically.
    "Disable resuming Shorts on startup", # Adds an option to disable the Shorts player from resuming on app startup when Shorts were last being watched.
    "Disable rolling number animations", # Adds an option to disable rolling number animations of video view count, user likes, and upload time.
    "Disable suggested video end screen", # Adds an option to disable the suggested video end screen at the end of videos.
    "GmsCore support", # Allows patched Google apps to run without root and under a different package name by using GmsCore instead of Google Play Services.
    "Hide 'Load more' button", # Adds an option to hide the button under videos that loads similar videos.
    "Hide ads", # Adds options to remove general ads.
    "Hide album cards", # Adds an option to hide album cards below artist descriptions.
    "Hide autoplay button", # Adds an option to hide the autoplay button in the video player.
    "Hide breaking news shelf", # Adds an option to hide the breaking news shelf on the homepage tab.
    "Hide cast button", # Adds an option to hide the cast button in the video player.
    "Hide crowdfunding box", # Adds an option to hide the crowdfunding box between the player and video description.
    "Hide endscreen cards", # Adds an option to hide suggested video cards at the end of videos.
    "Hide filter bar", # Adds options to hide the category bar at the top of video feeds.
    "Hide floating microphone button", # Adds an option to hide the floating microphone button when searching.
    "Hide layout components", # Adds options to hide general layout components.
    "Hide player buttons", # Adds an option to hide the previous and next buttons in the video player.
    "Hide Shorts components", # Adds options to hide components related to YouTube Shorts.
    "Hide video action buttons", # Adds options to hide action buttons (such as the Download button) under videos.
    "Minimized playback", # Unlocks options for picture-in-picture and background playback.
    "Navigation buttons", # Adds options to hide and change navigation buttons (such as the Shorts button).
    "Open links externally", # Adds an option to always open links in your browser instead of in the in-app-browser.
    "Player flyout menu", # Adds options to hide menu items that appear when pressing the gear icon in the video player.
    "Remember video quality", # Adds an option to remember the last video quality selected.
    "Remove player controls background", # Removes the dark background surrounding the video player controls.
    "Remove tracking query parameter", # Adds an option to remove the tracking info from links you share.
    "Remove viewer discretion dialog", # Adds an option to remove the dialog that appears when opening a video that has been age-restricted by accepting it automatically. This does not bypass the age restriction.
    "Restore old seekbar thumbnails", # Adds an option to restore the old seekbar thumbnails that appear above the seekbar while seeking instead of fullscreen thumbnails.
    "Restore old video quality menu", # Adds an option to restore the old video quality menu with specific video resolution options.
    "SponsorBlock", # Adds options to enable and configure SponsorBlock, which can skip undesired video segments such as sponsored content.
    "Spoof app version", # Adds an option to trick YouTube into thinking you are running an older version of the app. This can be used to restore old UI elements and features.
    "Theme", # Adds options for theming and applies a custom background theme (dark background theme defaults to amoled black).
    "Video ads", # Adds an option to remove ads in the video player.
    #"Always repeat", # Adds an option to always repeat videos when they end.
    #"Announcements", # Adds an option to show announcements from ReVanced on app startup.
    #"Change header", # Applies a custom header in the top left corner within the app. Defaults to the ReVanced header.
    #"Comments", # Adds options to hide components related to comments.
    #"Copy video URL", # Adds options to display buttons in the video player to copy video URLs.
    #"Custom branding", # Applies a custom app name and icon. Defaults to "YouTube ReVanced" and the ReVanced logo.
    #"Custom player overlay opacity", # Adds an option to change the opacity of the video player background when player controls are visible.
    #"Disable auto captions", # Adds an option to disable captions from being automatically enabled.
    #"Disable precise seeking gesture", # Adds an option to disable precise seeking when swiping up on the seekbar.
    #"Disable zoom haptics", # Adds an option to disable haptics when zooming.
    #"Enable debugging", # Adds options for debugging.
    #"Enable slide to seek", # Adds an option to enable slide to seek instead of playing at 2x speed when pressing and holding in the video player.  Including this patch may cause issues with tapping or double tapping the video player overlay.
    #"Enable tablet layout", # Adds an option to spoof the device form factor to a tablet which enables the tablet layout.
    #"External downloads", # Adds support to download and save YouTube videos using an external downloader app.
    #"HDR auto brightness", # Adds an option to make the brightness of HDR videos follow the system default.
    #"Hide captions button", # Adds an option to hide the captions button in the video player.
    #"Hide info cards", # Adds an option to hide info cards that creators add in the video player.
    #"Hide seekbar", # Adds an option to hide the seekbar.
    #"Hide timestamp", # Adds an option to hide the timestamp in the bottom left of the video player.
    #"Playback speed", # Adds options to customize available playback speeds and to remember the last playback speed selected.
    #"Return YouTube Dislike", # Adds an option to show the dislike count of videos using the Return YouTube Dislike API.
    #"Seekbar tapping", # Adds an option to enable tap-to-seek on the seekbar of the video player.
    #"Spoof device dimensions", # Adds an option to spoof the device dimensions which unlocks higher video qualities if they aren't available on the device.
    #"Swipe controls", # Adds options to enable and configure volume and brightness swipe controls.
    #"Tablet mini player", # Adds an option to enable the tablet mini player layout.
    #"Wide searchbar", # Adds an option to replace the search icon with a wide search bar. This will hide the YouTube logo when active.
]
