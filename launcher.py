import customtkinter as ctk
import minecraft_launcher_lib as mll
import minecraft_launcher_lib.microsoft_account as ms_account
import subprocess
import threading
import requests
import os
import json
import shutil
import zipfile
from PIL import Image
from tkinter import filedialog, messagebox
import webbrowser
import tkinter.simpledialog
import random
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

COLORS = {
    "bg": "#0A0B0E",
    "surface": "#111214",
    "card": "#1A1C1F",
    "card_hover": "#222529",
    "border": "#2A2D32",
    "primary": "#3B82F6",
    "primary_hover": "#2563EB",
    "secondary": "#6B7280",
    "success": "#10B981",
    "warning": "#F59E0B",
    "error": "#EF4444",
    "text": "#FFFFFF",
    "text_secondary": "#9CA3AF",
    "text_muted": "#6B7280",
    "purple": "#8B5CF6",
    "pink": "#EC4899",
    "orange": "#F97316",
    "cyan": "#06B6D4"
}

TEXTS = {
    "de": {
        "title": "MINECRAFT LAUNCHER",
        "version": "v2.0",
        "offline": "Offline",
        "online": "Online",
        "nav_dashboard": "🏠 Dashboard",
        "nav_play": "🎮 Spiel starten",
        "nav_skin": "🎨 Skin Studio",
        "nav_versions": "📦 Versionen",
        "nav_modpacks": "🔄 Modpacks",
        "nav_instances": "📁 Instanzen",
        "nav_settings": "⚙️ Einstellungen",
        "nav_stats": "📊 Statistiken",
        "welcome": "Willkommen zurück!",
        "stats_versions": "Versionen",
        "stats_modpacks": "Modpacks",
        "stats_instances": "Instanzen",
        "stats_player": "Spieler",
        "minecraft_news": "📰 Minecraft News",
        "quick_start": "Schnellstart",
        "quick_play": "▶ Minecraft starten",
        "quick_skin": "🎨 Skin wechseln",
        "play_title": "MINECRAFT STARTEN",
        "player": "Spieler",
        "not_logged_in": "Nicht angemeldet",
        "logged_in": "Angemeldet",
        "version": "Version",
        "instance": "Instanz",
        "ram": "Arbeitsspeicher",
        "ram_recommended": "Empfohlen: 2-4 GB | Maximal: 16 GB",
        "java": "Java",
        "options": "Optionen",
        "fullscreen": "Vollbild",
        "close_launcher": "Launcher nach Start schließen",
        "start_game": "MINECRAFT STARTEN",
        "ready": "Bereit",
        "starting": "Starte Minecraft...",
        "installing": "Installiere",
        "running": "Minecraft läuft!",
        "error_start": "Fehler beim Start",
        "skin_title": "SKIN STUDIO",
        "skin_preview": "Skin Vorschau",
        "skin_management": "Skin Verwaltung",
        "select_skin": "📁 Skin auswählen (PNG)",
        "upload_skin": "☁️ Zu Minecraft hochladen",
        "saved_skins": "Gespeicherte Skins",
        "no_skins": "Keine gespeicherten Skins",
        "steve": "Steve",
        "alex": "Alex",
        "skin_uploaded": "Skin wurde hochgeladen!",
        "versions_title": "VERSIONEN MANAGER",
        "installed_versions": "✅ Installierte Versionen",
        "available_versions": "📦 Verfügbare Versionen",
        "search_version": "🔍 Version suchen...",
        "search": "Suchen",
        "no_versions": "Keine Versionen installiert",
        "installed": "✓ Installiert",
        "install": "Installieren",
        "repair": "Reparieren",
        "modpacks_title": "MODPACKS & MODS",
        "category": "Kategorie:",
        "all": "Alle",
        "refresh": "🔄 Aktualisieren",
        "install_modpack": "Installieren",
        "installing_modpack": "Installiere Modpack...",
        "modpack_installed": "Modpack erfolgreich installiert!",
        "instances_title": "INSTANZEN",
        "new_instance": "+ Neue Instanz",
        "import_instance": "📁 Instanz importieren",
        "no_instances": "Keine Instanzen vorhanden\nErstelle eine neue Instanz",
        "play": "Spielen",
        "edit": "Bearbeiten",
        "settings_title": "EINSTELLUNGEN",
        "general": "Allgemein",
        "theme": "Design",
        "language": "Sprache",
        "minecraft_settings": "Minecraft",
        "java_path": "Java Pfad",
        "change": "Ändern",
        "minecraft_dir": "Minecraft Verzeichnis",
        "advanced": "Erweitert",
        "jvm_args": "Zusätzliche JVM Argumente",
        "logging": "Logging",
        "save_logs": "Logs speichern",
        "stats_title": "STATISTIKEN",
        "playtime": "⏱️ Spielzeit",
        "launches": "🎮 Gestartet",
        "system_info": "System Information",
        "os": "Betriebssystem",
        "python_version": "Python Version",
        "launcher_version": "Launcher Version",
        "minecraft_path": "Minecraft Pfad",
        "java_version": "Java",
        "recent_logs": "Letzte Logs",
        "error": "Fehler",
        "success": "Erfolg",
        "login_first": "Bitte zuerst anmelden!",
        "select_skin_first": "Bitte zuerst einen Skin auswählen!",
        "wait_versions": "Bitte warte bis die Versionen geladen sind!",
        "instance_created": "Instanz wurde erstellt!",
        "instance_imported": "Instanz wurde importiert!"
    },
    "en": {
        "title": "MINECRAFT LAUNCHER",
        "version": "v2.0",
        "offline": "Offline",
        "online": "Online",
        "nav_dashboard": "🏠 Dashboard",
        "nav_play": "🎮 Play",
        "nav_skin": "🎨 Skin Studio",
        "nav_versions": "📦 Versions",
        "nav_modpacks": "🔄 Modpacks",
        "nav_instances": "📁 Instances",
        "nav_settings": "⚙️ Settings",
        "nav_stats": "📊 Statistics",
        "welcome": "Welcome back!",
        "stats_versions": "Versions",
        "stats_modpacks": "Modpacks",
        "stats_instances": "Instances",
        "stats_player": "Player",
        "minecraft_news": "📰 Minecraft News",
        "quick_start": "Quick Start",
        "quick_play": "▶ Play Minecraft",
        "quick_skin": "🎨 Change Skin",
        "play_title": "PLAY MINECRAFT",
        "player": "Player",
        "not_logged_in": "Not logged in",
        "logged_in": "Logged in",
        "version": "Version",
        "instance": "Instance",
        "ram": "RAM",
        "ram_recommended": "Recommended: 2-4 GB | Maximum: 16 GB",
        "java": "Java",
        "options": "Options",
        "fullscreen": "Fullscreen",
        "close_launcher": "Close launcher after launch",
        "start_game": "PLAY MINECRAFT",
        "ready": "Ready",
        "starting": "Starting Minecraft...",
        "installing": "Installing",
        "running": "Minecraft is running!",
        "error_start": "Error starting",
        "skin_title": "SKIN STUDIO",
        "skin_preview": "Skin Preview",
        "skin_management": "Skin Management",
        "select_skin": "📁 Select Skin (PNG)",
        "upload_skin": "☁️ Upload to Minecraft",
        "saved_skins": "Saved Skins",
        "no_skins": "No saved skins",
        "steve": "Steve",
        "alex": "Alex",
        "skin_uploaded": "Skin uploaded successfully!",
        "versions_title": "VERSION MANAGER",
        "installed_versions": "✅ Installed Versions",
        "available_versions": "📦 Available Versions",
        "search_version": "🔍 Search version...",
        "search": "Search",
        "no_versions": "No versions installed",
        "installed": "✓ Installed",
        "install": "Install",
        "repair": "Repair",
        "modpacks_title": "MODPACKS & MODS",
        "category": "Category:",
        "all": "All",
        "refresh": "🔄 Refresh",
        "install_modpack": "Install",
        "installing_modpack": "Installing modpack...",
        "modpack_installed": "Modpack installed successfully!",
        "instances_title": "INSTANCES",
        "new_instance": "+ New Instance",
        "import_instance": "📁 Import Instance",
        "no_instances": "No instances found\nCreate a new instance",
        "play": "Play",
        "edit": "Edit",
        "settings_title": "SETTINGS",
        "general": "General",
        "theme": "Theme",
        "language": "Language",
        "minecraft_settings": "Minecraft",
        "java_path": "Java Path",
        "change": "Change",
        "minecraft_dir": "Minecraft Directory",
        "advanced": "Advanced",
        "jvm_args": "Additional JVM Arguments",
        "logging": "Logging",
        "save_logs": "Save logs",
        "stats_title": "STATISTICS",
        "playtime": "⏱️ Playtime",
        "launches": "🎮 Launches",
        "system_info": "System Information",
        "os": "Operating System",
        "python_version": "Python Version",
        "launcher_version": "Launcher Version",
        "minecraft_path": "Minecraft Path",
        "java_version": "Java",
        "recent_logs": "Recent Logs",
        "error": "Error",
        "success": "Success",
        "login_first": "Please login first!",
        "select_skin_first": "Please select a skin first!",
        "wait_versions": "Please wait for versions to load!",
        "instance_created": "Instance created!",
        "instance_imported": "Instance imported!"
    }
}

MODPACKS_DB = [
    {"name": "🔊 Simple Voice Chat", "version": "1.20.4", "loader": "Fabric", "icon": "🎤", "description": "Proximity Voice Chat für Minecraft", "downloads": "2.5M", "category": "Utility", "modrinth_id": "voicechat"},
    {"name": "📦 Just Enough Items (JEI)", "version": "1.20.4", "loader": "Fabric", "icon": "📋", "description": "Rezepte und Items anzeigen", "downloads": "45M", "category": "Utility", "modrinth_id": "jei"},
    {"name": "🗺️ Xaero's Minimap", "version": "1.20.4", "loader": "Fabric", "icon": "🗺️", "description": "Minimap mit Wegpunkten", "downloads": "12M", "category": "Utility", "modrinth_id": "xaeros-minimap"},
    {"name": "🗺️ Xaero's World Map", "version": "1.20.4", "loader": "Fabric", "icon": "🌍", "description": "Vollständige Weltkarte", "downloads": "8.5M", "category": "Utility", "modrinth_id": "xaeros-world-map"},
    {"name": "📊 MiniHUD", "version": "1.20.4", "loader": "Fabric", "icon": "📊", "description": "FPS, Koordinaten und mehr anzeigen", "downloads": "3.2M", "category": "Utility", "modrinth_id": "minihud"},
    {"name": "🔍 Waila / HWYLA", "version": "1.20.4", "loader": "Fabric", "icon": "🔍", "description": "Zeigt an was du anschaust", "downloads": "8.5M", "category": "Utility", "modrinth_id": "waila"},
    {"name": "🔍 Jade", "version": "1.20.4", "loader": "Fabric", "icon": "💎", "description": "Moderne Alternative zu Waila", "downloads": "4.2M", "category": "Utility", "modrinth_id": "jade"},
    {"name": "📦 Inventory Profiles Next", "version": "1.20.4", "loader": "Fabric", "icon": "📦", "description": "Automatisches Inventar-Management", "downloads": "4.2M", "category": "Utility", "modrinth_id": "inventory-profiles-next"},
    {"name": "⌨️ Controlling", "version": "1.20.4", "loader": "Fabric", "icon": "⌨️", "description": "Bessere Tastenbelegung", "downloads": "1.8M", "category": "Utility", "modrinth_id": "controlling"},
    {"name": "🔍 Zoomify", "version": "1.20.4", "loader": "Fabric", "icon": "🔍", "description": "Zoom-Funktion", "downloads": "3.2M", "category": "Utility", "modrinth_id": "zoomify"},
    {"name": "📸 Replay Mod", "version": "1.20.4", "loader": "Fabric", "icon": "🎥", "description": "Aufnahmen und Replays", "downloads": "3.5M", "category": "Utility", "modrinth_id": "replay-mod"},
    {"name": "🌍 WorldEdit", "version": "1.20.4", "loader": "Fabric", "icon": "🌍", "description": "Ingame Welt-Editier-Tools", "downloads": "6.2M", "category": "Utility", "modrinth_id": "worldedit"},
    {"name": "📋 Litematica", "version": "1.20.4", "loader": "Fabric", "icon": "📐", "description": "Baupläne und Schematica", "downloads": "2.1M", "category": "Utility", "modrinth_id": "litematica"},
    {"name": "🔧 Fabric API", "version": "1.20.4", "loader": "Fabric", "icon": "🔧", "description": "Basis für Fabric Mods", "downloads": "25M", "category": "Utility", "modrinth_id": "fabric-api"},
    {"name": "📦 Mod Menu", "version": "1.20.4", "loader": "Fabric", "icon": "📋", "description": "Mod-Übersicht im Menü", "downloads": "8.2M", "category": "Utility", "modrinth_id": "modmenu"},
    
    {"name": "⚡ Sodium", "version": "1.20.4", "loader": "Fabric", "icon": "⚡", "description": "Extreme Performance Optimierung", "downloads": "18M", "category": "Performance", "modrinth_id": "sodium"},
    {"name": "🔦 Iris Shaders", "version": "1.20.4", "loader": "Fabric", "icon": "✨", "description": "Shader-Unterstützung", "downloads": "8.5M", "category": "Performance", "modrinth_id": "iris"},
    {"name": "📦 Lithium", "version": "1.20.4", "loader": "Fabric", "icon": "🔋", "description": "Server-Performance Optimierung", "downloads": "12M", "category": "Performance", "modrinth_id": "lithium"},
    {"name": "🔄 Phosphor", "version": "1.20.4", "loader": "Fabric", "icon": "💡", "description": "Lighting Engine Optimierung", "downloads": "7.2M", "category": "Performance", "modrinth_id": "phosphor"},
    {"name": "💨 Starlight", "version": "1.20.4", "loader": "Fabric", "icon": "⭐", "description": "Bessere Lichtberechnung", "downloads": "5.8M", "category": "Performance", "modrinth_id": "starlight"},
    {"name": "🧲 FerriteCore", "version": "1.20.4", "loader": "Fabric", "icon": "🧲", "description": "Reduziert RAM-Nutzung", "downloads": "3.2M", "category": "Performance", "modrinth_id": "ferrite-core"},
    {"name": "📊 Spark", "version": "1.20.4", "loader": "Fabric", "icon": "🔥", "description": "Performance Profiler", "downloads": "1.5M", "category": "Performance", "modrinth_id": "spark"},
    {"name": "🎨 Enhanced Block Entities", "version": "1.20.4", "loader": "Fabric", "icon": "🎨", "description": "Optimierte Block-Entities", "downloads": "2.3M", "category": "Performance", "modrinth_id": "ebe"},
    {"name": "⚡ CullLessLeaves", "version": "1.20.4", "loader": "Fabric", "icon": "🍃", "description": "Optimierte Blatt-Rendering", "downloads": "1.1M", "category": "Performance", "modrinth_id": "cull-less-leaves"},
    {"name": "💨 Entity Culling", "version": "1.20.4", "loader": "Fabric", "icon": "👻", "description": "Unsichtbare Entities cullen", "downloads": "2.8M", "category": "Performance", "modrinth_id": "entityculling"},
    
    {"name": "✨ Mouse Tweaks", "version": "1.20.4", "loader": "Fabric", "icon": "🐭", "description": "Verbesserte Maus-Steuerung", "downloads": "4.2M", "category": "QoL", "modrinth_id": "mouse-tweaks"},
    {"name": "🍎 AppleSkin", "version": "1.20.4", "loader": "Fabric", "icon": "🍎", "description": "Bessere Nahrungs-Anzeige", "downloads": "3.8M", "category": "QoL", "modrinth_id": "appleskin"},
    {"name": "🛠️ Tool Stats", "version": "1.20.4", "loader": "Fabric", "icon": "🛠️", "description": "Werkzeug-Informationen", "downloads": "1.2M", "category": "QoL", "modrinth_id": "tool-stats"},
    {"name": "📝 BetterF3", "version": "1.20.4", "loader": "Fabric", "icon": "📊", "description": "Schönere F3-Anzeige", "downloads": "2.5M", "category": "QoL", "modrinth_id": "betterf3"},
    {"name": "💬 Chat Heads", "version": "1.20.4", "loader": "Fabric", "icon": "💬", "description": "Spieler-Köpfe im Chat", "downloads": "1.8M", "category": "QoL", "modrinth_id": "chat-heads"},
    {"name": "🔊 Sound Physics", "version": "1.20.4", "loader": "Fabric", "icon": "🔊", "description": "Realistischere Sound-Effekte", "downloads": "1.2M", "category": "QoL", "modrinth_id": "sound-physics"},
    {"name": "🌙 Night Vision", "version": "1.20.4", "loader": "Fabric", "icon": "🌙", "description": "Toggle Night Vision", "downloads": "900K", "category": "QoL", "modrinth_id": "night-vision"},
    {"name": "🚀 Boosted Brightness", "version": "1.20.4", "loader": "Fabric", "icon": "☀️", "description": "Extra Helligkeitsstufen", "downloads": "750K", "category": "QoL", "modrinth_id": "boosted-brightness"},
    
    {"name": "🎨 Complementary Shaders", "version": "1.20.4", "loader": "Fabric", "icon": "🎨", "description": "Wunderschöne Shader", "downloads": "5.2M", "category": "Visual", "modrinth_id": "complementary-shaders"},
    {"name": "🦊 Fresh Animations", "version": "1.20.4", "loader": "Fabric", "icon": "🦊", "description": "Verbesserte Animationen", "downloads": "2.8M", "category": "Visual", "modrinth_id": "fresh-animations"},
    {"name": "🖼️ Continuity", "version": "1.20.4", "loader": "Fabric", "icon": "🖼️", "description": "Connected Textures", "downloads": "1.5M", "category": "Visual", "modrinth_id": "continuity"},
    {"name": "🌿 Better Clouds", "version": "1.20.4", "loader": "Fabric", "icon": "☁️", "description": "Schönere Wolken", "downloads": "1.2M", "category": "Visual", "modrinth_id": "better-clouds"},
    {"name": "🍂 Falling Leaves", "version": "1.20.4", "loader": "Fabric", "icon": "🍂", "description": "Fallende Blätter", "downloads": "950K", "category": "Visual", "modrinth_id": "falling-leaves"},
    {"name": "✨ Visuality", "version": "1.20.4", "loader": "Fabric", "icon": "✨", "description": "Atmosphärische Effekte", "downloads": "800K", "category": "Visual", "modrinth_id": "visuality"},
    {"name": "🎨 BSL Shaders", "version": "1.20.4", "loader": "Fabric", "icon": "🎨", "description": "Beliebte Shader", "downloads": "4.5M", "category": "Visual", "modrinth_id": "bsl-shaders"},
    {"name": "🌟 SEUS Shaders", "version": "1.20.4", "loader": "Fabric", "icon": "🌟", "description": "Realistische Shader", "downloads": "3.8M", "category": "Visual", "modrinth_id": "seus"},
    
    {"name": "Vanilla+", "version": "1.20.4", "loader": "Vanilla", "icon": "🎮", "description": "Verbesserte Vanilla Erfahrung", "downloads": "1.2M", "category": "Vanilla+"},
    {"name": "Vanilla Tweaks", "version": "1.20.4", "loader": "Vanilla", "icon": "🔧", "description": "Vanilla mit kleinen Verbesserungen", "downloads": "856K", "category": "Vanilla+"},
    {"name": "Quality of Life", "version": "1.20.1", "loader": "Fabric", "icon": "✨", "description": "Nützliche Verbesserungen", "downloads": "523K", "category": "Vanilla+"},
    
    {"name": "Better MC [FORGE]", "version": "1.20.1", "loader": "Forge", "icon": "⚔️", "description": "Das ultimative Vanilla+ Erlebnis", "downloads": "4.2M", "category": "Forge"},
    {"name": "RLCraft", "version": "1.12.2", "loader": "Forge", "icon": "🐉", "description": "Extrem schweres Survival", "downloads": "8.5M", "category": "Forge"},
    {"name": "SkyFactory 4", "version": "1.12.2", "loader": "Forge", "icon": "☁️", "description": "Baue deine Welt in der Sky", "downloads": "3.1M", "category": "Forge"},
    {"name": "All The Mods 9", "version": "1.20.1", "loader": "Forge", "icon": "🔮", "description": "Über 400 Mods", "downloads": "2.8M", "category": "Forge"},
    {"name": "Pixelmon Reforged", "version": "1.16.5", "loader": "Forge", "icon": "🎯", "description": "Pokémon in Minecraft", "downloads": "6.2M", "category": "Forge"},
    {"name": "Roguelike Adventures", "version": "1.16.5", "loader": "Forge", "icon": "🏰", "description": "Roguelike Dungeon Crawler", "downloads": "1.5M", "category": "Forge"},
    {"name": "Medieval Minecraft", "version": "1.19.2", "loader": "Forge", "icon": "🏯", "description": "Mittelalterliches Fantasy", "downloads": "1.8M", "category": "Forge"},
    {"name": "Create: Above and Beyond", "version": "1.18.2", "loader": "Forge", "icon": "🔧", "description": "Create Mod Quest Pack", "downloads": "1.2M", "category": "Forge"},
    {"name": "Valhelsia 6", "version": "1.19.2", "loader": "Forge", "icon": "🌲", "description": "Exploration & Technologie", "downloads": "987K", "category": "Forge"},
    {"name": "Enigmatica 9", "version": "1.19.2", "loader": "Forge", "icon": "❓", "description": "Quest-basiertes Modpack", "downloads": "1.1M", "category": "Forge"},
    
    {"name": "Fabulously Optimized", "version": "1.20.4", "loader": "Fabric", "icon": "✨", "description": "Optimiertes Vanilla", "downloads": "3.2M", "category": "Fabric"},
    {"name": "Simply Optimized", "version": "1.20.4", "loader": "Fabric", "icon": "⚡", "description": "Nur Performance Mods", "downloads": "1.5M", "category": "Fabric"},
    {"name": "Create: Perfect World", "version": "1.20.1", "loader": "Fabric", "icon": "🔧", "description": "Create Mod + Optimierungen", "downloads": "856K", "category": "Fabric"},
    {"name": "Better Minecraft [FABRIC]", "version": "1.20.1", "loader": "Fabric", "icon": "⚔️", "description": "Vanilla+ mit Fabric", "downloads": "1.2M", "category": "Fabric"},
    {"name": "All of Fabric 6", "version": "1.19.2", "loader": "Fabric", "icon": "🔮", "description": "Großes Fabric Modpack", "downloads": "987K", "category": "Fabric"},
    {"name": "Adventures in Fabric", "version": "1.20.1", "loader": "Fabric", "icon": "🗺️", "description": "Exploration & Abenteuer", "downloads": "456K", "category": "Fabric"},
    {"name": "Fabric Skyblock", "version": "1.19.2", "loader": "Fabric", "icon": "☁️", "description": "Skyblock mit Fabric Mods", "downloads": "234K", "category": "Fabric"},
    
    {"name": "Craft to Exile 2", "version": "1.20.1", "loader": "Forge", "icon": "🗡️", "description": "ARPG Experience", "downloads": "678K", "category": "Adventure"},
    {"name": "Dimension Hopper", "version": "1.19.2", "loader": "Fabric", "icon": "🌌", "description": "Dimensionen erkunden", "downloads": "123K", "category": "Adventure"},
    {"name": "The Betweenlands", "version": "1.12.2", "loader": "Forge", "icon": "🌿", "description": "Düstere Sumpfwelt", "downloads": "890K", "category": "Adventure"},
    {"name": "Vault Hunters 3", "version": "1.18.2", "loader": "Forge", "icon": "🏛️", "description": "RPG Dungeon Crawler", "downloads": "1.2M", "category": "Adventure"},
    
    {"name": "Nomifactory", "version": "1.12.2", "loader": "Forge", "icon": "🏭", "description": "GregTech-basiert", "downloads": "456K", "category": "Technology"},
    {"name": "Compact Claustrophobia", "version": "1.16.5", "loader": "Forge", "icon": "📦", "description": "Skyblock in einem Raum", "downloads": "234K", "category": "Technology"},
    {"name": "Mechanical Mastery", "version": "1.18.2", "loader": "Forge", "icon": "⚙️", "description": "Automatisierung Fokus", "downloads": "156K", "category": "Technology"},
    
    {"name": "SkyFactory 5", "version": "1.20.1", "loader": "Forge", "icon": "☁️", "description": "Neueste SkyFactory", "downloads": "567K", "category": "Skyblock"},
    {"name": "Project Ozone 4", "version": "1.12.2", "loader": "Forge", "icon": "🌌", "description": "Extrem Skyblock", "downloads": "789K", "category": "Skyblock"},
    {"name": "Stoneblock 3", "version": "1.18.2", "loader": "Forge", "icon": "🪨", "description": "In einem Steinblock", "downloads": "1.1M", "category": "Skyblock"},
    
    {"name": "GregTech: New Horizons", "version": "1.7.10", "loader": "Forge", "icon": "🏭", "description": "Extrem schweres Technik", "downloads": "890K", "category": "Challenging"},
    {"name": "SevTech: Ages", "version": "1.12.2", "loader": "Forge", "icon": "📜", "description": "Fortschritt durch Zeitalter", "downloads": "1.4M", "category": "Challenging"},
    {"name": "Rebirth of the Night", "version": "1.12.2", "loader": "Forge", "icon": "🌙", "description": "Survival Herausforderung", "downloads": "456K", "category": "Challenging"},
    
    {"name": "Ars Nouveau", "version": "1.20.1", "loader": "Forge", "icon": "📖", "description": "Zauberei & Magie", "downloads": "345K", "category": "Magic"},
    {"name": "Bewitchment", "version": "1.19.2", "loader": "Fabric", "icon": "🧙", "description": "Hexerei & Magie", "downloads": "234K", "category": "Magic"},
    {"name": "Iron's Spells", "version": "1.20.1", "loader": "Forge", "icon": "⚡", "description": "Zauber & Sprüche", "downloads": "456K", "category": "Magic"},
    
    {"name": "FPS Boost", "version": "1.20.4", "loader": "Fabric", "icon": "⚡", "description": "Nur Performance", "downloads": "2.1M", "category": "Lightweight"},
    {"name": "QoL+", "version": "1.20.4", "loader": "Fabric", "icon": "✨", "description": "Nützliche Mods", "downloads": "456K", "category": "Lightweight"},
    {"name": "Minimal", "version": "1.20.4", "loader": "Vanilla", "icon": "🎮", "description": "Minimalistisch", "downloads": "234K", "category": "Lightweight"},
]

MODPACK_CATEGORIES = ["Alle", "Utility", "Performance", "QoL", "Visual", "Vanilla+", "Forge", "Fabric", "Adventure", "Technology", "Skyblock", "Challenging", "Magic", "Lightweight"]


class MinecraftLauncher:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Minecraft Launcher")
        self.window.geometry("1400x850")
        self.window.minsize(1200, 750)
        self.window.configure(fg_color=COLORS["bg"])
        
        self.current_lang = "de"
        
        self.login_data = None
        self.is_logged_in = False
        self.selected_skin_path = None
        self.versions = []
        self.installed_versions = []
        self.modpacks = MODPACKS_DB.copy()
        self.instances = []
        self.java_path = self.find_java()
        
        self.playtime_minutes = 0
        self.launch_count = 0
        
        self.minecraft_dir = mll.utils.get_minecraft_directory()
        self.launcher_dir = os.path.join(os.path.dirname(__file__), ".launcher")
        self.instances_dir = os.path.join(self.launcher_dir, "instances")
        self.modpacks_dir = os.path.join(self.launcher_dir, "modpacks")
        self.skins_dir = os.path.join(self.launcher_dir, "skins")
        self.logs_dir = os.path.join(self.launcher_dir, "logs")
        self.cache_dir = os.path.join(self.launcher_dir, "cache")
        
        for dir_path in [self.launcher_dir, self.instances_dir, self.modpacks_dir, 
                         self.skins_dir, self.logs_dir, self.cache_dir]:
            os.makedirs(dir_path, exist_ok=True)
        
        self.load_stats()
        self.setup_layout()
        self.load_versions()
        self.load_installed_versions()
        self.load_instances()
        self.check_saved_login()
        self.check_news()
        self.update_all_texts()
    
    def t(self, key):
        return TEXTS[self.current_lang].get(key, key)
    
    def find_java(self):
        java_paths = [
            "C:\\Program Files\\Java\\jre1.8.0_321\\bin\\javaw.exe",
            "C:\\Program Files\\Java\\jre1.8.0_311\\bin\\javaw.exe",
            "C:\\Program Files (x86)\\Java\\jre1.8.0_321\\bin\\javaw.exe",
            "C:\\Program Files\\Java\\jdk-17\\bin\\javaw.exe",
        ]
        for path in java_paths:
            if os.path.exists(path):
                return path
        import shutil
        java_path = shutil.which("javaw")
        return java_path if java_path else "javaw"
    
    def load_stats(self):
        stats_file = os.path.join(self.launcher_dir, "stats.json")
        if os.path.exists(stats_file):
            try:
                with open(stats_file, "r") as f:
                    stats = json.load(f)
                    self.playtime_minutes = stats.get("playtime", 0)
                    self.launch_count = stats.get("launches", 0)
            except:
                pass
    
    def save_stats(self):
        stats_file = os.path.join(self.launcher_dir, "stats.json")
        with open(stats_file, "w") as f:
            json.dump({"playtime": self.playtime_minutes, "launches": self.launch_count}, f)
    
    def setup_layout(self):
        sidebar = ctk.CTkFrame(self.window, width=260, fg_color=COLORS["surface"], corner_radius=0)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)
        
        logo_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        logo_frame.pack(pady=25)
        self.logo_label = ctk.CTkLabel(logo_frame, text="⛏️ MINECRAFT", font=("Inter", 20, "bold"), text_color=COLORS["primary"])
        self.logo_label.pack()
        self.launcher_badge = ctk.CTkLabel(logo_frame, text="LAUNCHER", font=("Inter", 10), text_color=COLORS["text_secondary"], corner_radius=10, fg_color=COLORS["card"], padx=8, pady=2)
        self.launcher_badge.pack(pady=(5, 0))
        
        nav_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        nav_frame.pack(pady=30, padx=15, fill="x")
        
        self.nav_buttons = {}
        nav_items = [
            ("nav_dashboard", "dashboard"),
            ("nav_play", "play"),
            ("nav_skin", "skin"),
            ("nav_versions", "versions"),
            ("nav_modpacks", "modpacks"),
            ("nav_instances", "instances"),
            ("nav_settings", "settings"),
            ("nav_stats", "stats")
        ]
        
        for text_key, key in nav_items:
            btn = ctk.CTkButton(nav_frame, text=self.t(text_key), font=("Inter", 13), height=40, fg_color="transparent", hover_color=COLORS["card_hover"], anchor="w", corner_radius=8, command=lambda k=key: self.show_page(k))
            btn.pack(pady=2, fill="x")
            self.nav_buttons[key] = btn
        
        user_frame = ctk.CTkFrame(sidebar, fg_color=COLORS["card"], corner_radius=12)
        user_frame.pack(side="bottom", pady=20, padx=15, fill="x")
        
        self.user_avatar = ctk.CTkLabel(user_frame, text="👤", font=("Inter", 28))
        self.user_avatar.pack(pady=(15, 5))
        self.user_name_label = ctk.CTkLabel(user_frame, text="Offline-Spieler", font=("Inter", 12, "bold"), text_color=COLORS["text"])
        self.user_name_label.pack()
        self.user_status_label = ctk.CTkLabel(user_frame, text=self.t("not_logged_in"), font=("Inter", 10), text_color=COLORS["text_muted"])
        self.user_status_label.pack()
        self.login_btn = ctk.CTkButton(user_frame, text="Anmelden", command=self.microsoft_login, height=32, font=("Inter", 11, "bold"), fg_color=COLORS["primary"], corner_radius=8)
        self.login_btn.pack(pady=(10, 15), padx=15, fill="x")
        
        self.main_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        self.main_frame.pack(side="right", fill="both", expand=True, padx=15, pady=15)
        
        self.pages = {}
        self.create_dashboard_page()
        self.create_play_page()
        self.create_skin_page()
        self.create_versions_page()
        self.create_modpacks_page()
        self.create_instances_page()
        self.create_settings_page()
        self.create_stats_page()
        
        self.show_page("dashboard")
    
    def create_dashboard_page(self):
        page = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        page.pack(fill="both", expand=True)
        
        header = ctk.CTkFrame(page, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))
        
        self.welcome_label = ctk.CTkLabel(header, text=self.t("welcome"), font=("Inter", 28, "bold"), text_color=COLORS["text"])
        self.welcome_label.pack(anchor="w")
        self.date_label = ctk.CTkLabel(header, text=datetime.now().strftime("%A, %d. %B %Y"), font=("Inter", 12), text_color=COLORS["text_muted"])
        self.date_label.pack(anchor="w")
        
        stats_grid = ctk.CTkFrame(page, fg_color="transparent")
        stats_grid.pack(fill="x", pady=20)
        for i in range(4):
            stats_grid.grid_columnconfigure(i, weight=1)
        
        stats = [
            ("stats_versions", "0", COLORS["primary"]),
            ("stats_modpacks", str(len(self.modpacks)), COLORS["purple"]),
            ("stats_instances", "0", COLORS["pink"]),
            ("stats_player", "Offline", COLORS["orange"])
        ]
        self.stats_labels = {}
        for i, (key, value, color) in enumerate(stats):
            card = ctk.CTkFrame(stats_grid, fg_color=COLORS["card"], corner_radius=12)
            card.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
            title = ctk.CTkLabel(card, text=self.t(key), font=("Inter", 11), text_color=COLORS["text_muted"])
            title.pack(pady=(15, 5))
            val = ctk.CTkLabel(card, text=value, font=("Inter", 24, "bold"), text_color=color)
            val.pack(pady=(0, 15))
            self.stats_labels[key] = val
        
        news_frame = ctk.CTkFrame(page, fg_color=COLORS["card"], corner_radius=12)
        news_frame.pack(fill="both", expand=True, pady=10)
        self.news_header = ctk.CTkLabel(news_frame, text=self.t("minecraft_news"), font=("Inter", 14, "bold"), text_color=COLORS["text"])
        self.news_header.pack(anchor="w", padx=15, pady=(15, 10))
        self.news_text = ctk.CTkTextbox(news_frame, font=("Inter", 11), fg_color="transparent", height=200)
        self.news_text.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        self.news_text.insert("1.0", "Lade Neuigkeiten...")
        self.news_text.configure(state="disabled")
        
        quick_frame = ctk.CTkFrame(page, fg_color="transparent")
        quick_frame.pack(fill="x", pady=10)
        self.quick_label = ctk.CTkLabel(quick_frame, text=self.t("quick_start"), font=("Inter", 12, "bold"))
        self.quick_label.pack(anchor="w", pady=(0, 10))
        btn_frame = ctk.CTkFrame(quick_frame, fg_color="transparent")
        btn_frame.pack(fill="x")
        self.quick_play_btn = ctk.CTkButton(btn_frame, text=self.t("quick_play"), command=lambda: self.show_page("play"), height=45, font=("Inter", 13, "bold"), fg_color=COLORS["success"], corner_radius=10)
        self.quick_play_btn.pack(side="left", padx=(0, 10))
        self.quick_skin_btn = ctk.CTkButton(btn_frame, text=self.t("quick_skin"), command=lambda: self.show_page("skin"), height=45, font=("Inter", 13), fg_color=COLORS["primary"], corner_radius=10)
        self.quick_skin_btn.pack(side="left")
        
        self.pages["dashboard"] = page
    
    def create_play_page(self):
        page = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        page.pack(fill="both", expand=True)
        
        self.play_title = ctk.CTkLabel(page, text=self.t("play_title"), font=("Inter", 24, "bold"), text_color=COLORS["text"])
        self.play_title.pack(anchor="w", pady=(0, 20))
        
        main = ctk.CTkFrame(page, fg_color="transparent")
        main.pack(fill="both", expand=True)
        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=1)
        
        left = ctk.CTkFrame(main, fg_color=COLORS["card"], corner_radius=12)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        self.play_player_title = ctk.CTkLabel(left, text=self.t("player"), font=("Inter", 14, "bold"), text_color=COLORS["text_secondary"])
        self.play_player_title.pack(anchor="w", padx=20, pady=(20, 10))
        self.play_player_name = ctk.CTkLabel(left, text="Offline-Spieler", font=("Inter", 16, "bold"), text_color=COLORS["text"])
        self.play_player_name.pack(anchor="w", padx=20)
        self.play_player_status = ctk.CTkLabel(left, text=self.t("not_logged_in"), font=("Inter", 11), text_color=COLORS["text_muted"])
        self.play_player_status.pack(anchor="w", padx=20, pady=(5, 20))
        
        self.play_version_title = ctk.CTkLabel(left, text=self.t("version"), font=("Inter", 14, "bold"), text_color=COLORS["text_secondary"])
        self.play_version_title.pack(anchor="w", padx=20, pady=(0, 10))
        self.play_version_menu = ctk.CTkOptionMenu(left, values=["Lade Versionen..."], height=45, font=("Inter", 13), fg_color=COLORS["bg"], button_color=COLORS["primary"], corner_radius=10)
        self.play_version_menu.pack(fill="x", padx=20, pady=(0, 15))
        
        self.play_instance_title = ctk.CTkLabel(left, text=self.t("instance"), font=("Inter", 14, "bold"), text_color=COLORS["text_secondary"])
        self.play_instance_title.pack(anchor="w", padx=20, pady=(0, 10))
        self.play_instance_menu = ctk.CTkOptionMenu(left, values=["Standard"], height=45, font=("Inter", 13), fg_color=COLORS["bg"], button_color=COLORS["secondary"], corner_radius=10)
        self.play_instance_menu.pack(fill="x", padx=20, pady=(0, 20))
        
        right = ctk.CTkFrame(main, fg_color=COLORS["card"], corner_radius=12)
        right.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        
        self.play_ram_title = ctk.CTkLabel(right, text=self.t("ram"), font=("Inter", 14, "bold"), text_color=COLORS["text_secondary"])
        self.play_ram_title.pack(anchor="w", padx=20, pady=(20, 10))
        ram_frame = ctk.CTkFrame(right, fg_color="transparent")
        ram_frame.pack(fill="x", padx=20, pady=(0, 5))
        self.play_ram_slider = ctk.CTkSlider(ram_frame, from_=1024, to=16384, number_of_steps=15, height=6, fg_color=COLORS["bg"], progress_color=COLORS["primary"])
        self.play_ram_slider.set(2048)
        self.play_ram_slider.pack(side="left", expand=True, fill="x", padx=(0, 15))
        self.play_ram_label = ctk.CTkLabel(ram_frame, text="2 GB", font=("Inter", 12, "bold"), text_color=COLORS["primary"])
        self.play_ram_label.pack(side="right")
        self.play_ram_slider.configure(command=self.update_ram_label)
        self.play_ram_info = ctk.CTkLabel(right, text=self.t("ram_recommended"), font=("Inter", 9), text_color=COLORS["text_muted"])
        self.play_ram_info.pack(anchor="w", padx=20)
        
        self.play_java_title = ctk.CTkLabel(right, text=self.t("java"), font=("Inter", 14, "bold"), text_color=COLORS["text_secondary"])
        self.play_java_title.pack(anchor="w", padx=20, pady=(20, 10))
        self.java_path_label = ctk.CTkLabel(right, text=f"Java: {os.path.basename(self.java_path)}", font=("Inter", 11), text_color=COLORS["text_muted"])
        self.java_path_label.pack(anchor="w", padx=20)
        
        self.play_options_title = ctk.CTkLabel(right, text=self.t("options"), font=("Inter", 14, "bold"), text_color=COLORS["text_secondary"])
        self.play_options_title.pack(anchor="w", padx=20, pady=(20, 10))
        self.fullscreen_var = ctk.BooleanVar(value=True)
        self.fullscreen_check = ctk.CTkCheckBox(right, text=self.t("fullscreen"), variable=self.fullscreen_var, font=("Inter", 11), fg_color=COLORS["primary"])
        self.fullscreen_check.pack(anchor="w", padx=20, pady=2)
        self.launcher_visibility_var = ctk.BooleanVar(value=False)
        self.visibility_check = ctk.CTkCheckBox(right, text=self.t("close_launcher"), variable=self.launcher_visibility_var, font=("Inter", 11), fg_color=COLORS["primary"])
        self.visibility_check.pack(anchor="w", padx=20, pady=2)
        
        self.play_start_btn = ctk.CTkButton(right, text=self.t("start_game"), command=self.start_minecraft, height=55, font=("Inter", 16, "bold"), fg_color=COLORS["success"], corner_radius=12)
        self.play_start_btn.pack(pady=(30, 20), padx=20, fill="x")
        self.play_status = ctk.CTkLabel(right, text=self.t("ready"), font=("Inter", 11), text_color=COLORS["text_muted"])
        self.play_status.pack(pady=(0, 20))
        
        self.pages["play"] = page
    
    def create_skin_page(self):
        page = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        page.pack(fill="both", expand=True)
        
        self.skin_title = ctk.CTkLabel(page, text=self.t("skin_title"), font=("Inter", 24, "bold"), text_color=COLORS["text"])
        self.skin_title.pack(anchor="w", pady=(0, 20))
        
        main = ctk.CTkFrame(page, fg_color="transparent")
        main.pack(fill="both", expand=True)
        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=1)
        
        preview_frame = ctk.CTkFrame(main, fg_color=COLORS["card"], corner_radius=12)
        preview_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        self.skin_preview_title = ctk.CTkLabel(preview_frame, text=self.t("skin_preview"), font=("Inter", 14, "bold"), text_color=COLORS["text_secondary"])
        self.skin_preview_title.pack(anchor="w", padx=20, pady=(20, 15))
        self.skin_preview_container = ctk.CTkFrame(preview_frame, fg_color=COLORS["bg"], corner_radius=12, height=250)
        self.skin_preview_container.pack(padx=20, pady=10, fill="x")
        self.skin_preview_container.pack_propagate(False)
        self.skin_preview_label = ctk.CTkLabel(self.skin_preview_container, text="👤\nKein Skin", font=("Inter", 36), text_color=COLORS["text_muted"])
        self.skin_preview_label.pack(expand=True, fill="both")
        self.skin_name_label = ctk.CTkLabel(preview_frame, text="Kein Skin ausgewählt", font=("Inter", 11), text_color=COLORS["text_muted"])
        self.skin_name_label.pack(pady=5)
        
        model_frame = ctk.CTkFrame(preview_frame, fg_color="transparent")
        model_frame.pack(pady=15)
        self.skin_model_var = ctk.StringVar(value="CLASSIC")
        self.steve_skin_btn = ctk.CTkButton(model_frame, text=self.t("steve"), width=80, height=32, fg_color=COLORS["primary"], command=lambda: self.set_skin_model("CLASSIC"))
        self.steve_skin_btn.pack(side="left", padx=5)
        self.alex_skin_btn = ctk.CTkButton(model_frame, text=self.t("alex"), width=80, height=32, fg_color=COLORS["secondary"], command=lambda: self.set_skin_model("SLIM"))
        self.alex_skin_btn.pack(side="left", padx=5)
        
        manage_frame = ctk.CTkFrame(main, fg_color=COLORS["card"], corner_radius=12)
        manage_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        self.skin_manage_title = ctk.CTkLabel(manage_frame, text=self.t("skin_management"), font=("Inter", 14, "bold"), text_color=COLORS["text_secondary"])
        self.skin_manage_title.pack(anchor="w", padx=20, pady=(20, 15))
        self.select_skin_btn = ctk.CTkButton(manage_frame, text=self.t("select_skin"), command=self.select_skin, height=45, font=("Inter", 13, "bold"), fg_color=COLORS["primary"], corner_radius=10)
        self.select_skin_btn.pack(padx=20, pady=5, fill="x")
        self.skin_upload_btn = ctk.CTkButton(manage_frame, text=self.t("upload_skin"), command=self.upload_skin, height=40, font=("Inter", 12), fg_color=COLORS["secondary"], state="disabled", corner_radius=10)
        self.skin_upload_btn.pack(padx=20, pady=5, fill="x")
        
        self.saved_skins_title = ctk.CTkLabel(manage_frame, text=self.t("saved_skins"), font=("Inter", 12, "bold"), text_color=COLORS["text_secondary"])
        self.saved_skins_title.pack(anchor="w", padx=20, pady=(20, 10))
        self.skins_scroll = ctk.CTkScrollableFrame(manage_frame, fg_color=COLORS["bg"], corner_radius=10, height=250)
        self.skins_scroll.pack(padx=20, pady=5, fill="both", expand=True)
        self.load_saved_skins()
        
        self.pages["skin"] = page
    
    def create_versions_page(self):
        page = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        page.pack(fill="both", expand=True)
        
        self.versions_title = ctk.CTkLabel(page, text=self.t("versions_title"), font=("Inter", 24, "bold"), text_color=COLORS["text"])
        self.versions_title.pack(anchor="w", pady=(0, 20))
        
        main = ctk.CTkFrame(page, fg_color="transparent")
        main.pack(fill="both", expand=True)
        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=1)
        
        installed_frame = ctk.CTkFrame(main, fg_color=COLORS["card"], corner_radius=12)
        installed_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        self.installed_title = ctk.CTkLabel(installed_frame, text=self.t("installed_versions"), font=("Inter", 14, "bold"), text_color=COLORS["success"])
        self.installed_title.pack(anchor="w", padx=20, pady=(20, 10))
        self.installed_scroll = ctk.CTkScrollableFrame(installed_frame, fg_color=COLORS["bg"], corner_radius=10)
        self.installed_scroll.pack(padx=20, pady=10, fill="both", expand=True)
        
        available_frame = ctk.CTkFrame(main, fg_color=COLORS["card"], corner_radius=12)
        available_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        self.available_title = ctk.CTkLabel(available_frame, text=self.t("available_versions"), font=("Inter", 14, "bold"), text_color=COLORS["primary"])
        self.available_title.pack(anchor="w", padx=20, pady=(20, 10))
        
        search_frame = ctk.CTkFrame(available_frame, fg_color="transparent")
        search_frame.pack(fill="x", padx=20, pady=(0, 10))
        self.version_search = ctk.CTkEntry(search_frame, placeholder_text=self.t("search_version"), font=("Inter", 12), height=35, fg_color=COLORS["bg"])
        self.version_search.pack(side="left", expand=True, fill="x", padx=(0, 10))
        self.search_btn = ctk.CTkButton(search_frame, text=self.t("search"), width=70, height=35, font=("Inter", 11), fg_color=COLORS["primary"], command=lambda: self.filter_versions(self.version_search.get()))
        self.search_btn.pack(side="right")
        
        self.available_scroll = ctk.CTkScrollableFrame(available_frame, fg_color=COLORS["bg"], corner_radius=10)
        self.available_scroll.pack(padx=20, pady=10, fill="both", expand=True)
        
        self.version_progress = ctk.CTkProgressBar(available_frame, height=6, fg_color=COLORS["bg"], progress_color=COLORS["success"])
        self.version_progress.pack(padx=20, pady=5, fill="x")
        self.version_progress.set(0)
        self.version_status = ctk.CTkLabel(available_frame, text="", font=("Inter", 10), text_color=COLORS["text_muted"])
        self.version_status.pack(pady=(0, 15))
        
        self.pages["versions"] = page
    
    def create_modpacks_page(self):
        page = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        page.pack(fill="both", expand=True)
        
        self.modpacks_title = ctk.CTkLabel(page, text=self.t("modpacks_title"), font=("Inter", 24, "bold"), text_color=COLORS["text"])
        self.modpacks_title.pack(anchor="w", pady=(0, 20))
        
        filter_frame = ctk.CTkFrame(page, fg_color="transparent")
        filter_frame.pack(fill="x", pady=(0, 15))
        self.filter_label = ctk.CTkLabel(filter_frame, text=self.t("category"), font=("Inter", 12))
        self.filter_label.pack(side="left", padx=(0, 10))
        self.modpack_filter = ctk.CTkOptionMenu(filter_frame, values=MODPACK_CATEGORIES, width=140, height=32, font=("Inter", 11), fg_color=COLORS["card"], command=self.filter_modpacks)
        self.modpack_filter.pack(side="left")
        self.refresh_btn = ctk.CTkButton(filter_frame, text=self.t("refresh"), width=120, height=32, font=("Inter", 11), fg_color=COLORS["secondary"], command=self.load_modpacks)
        self.refresh_btn.pack(side="right")
        
        self.modpacks_grid = ctk.CTkScrollableFrame(page, fg_color="transparent")
        self.modpacks_grid.pack(fill="both", expand=True)
        for i in range(4):
            self.modpacks_grid.grid_columnconfigure(i, weight=1)
        
        self.pages["modpacks"] = page
        self.display_modpacks()
    
    def create_instances_page(self):
        page = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        page.pack(fill="both", expand=True)
        
        self.instances_title = ctk.CTkLabel(page, text=self.t("instances_title"), font=("Inter", 24, "bold"), text_color=COLORS["text"])
        self.instances_title.pack(anchor="w", pady=(0, 20))
        
        btn_frame = ctk.CTkFrame(page, fg_color="transparent")
        btn_frame.pack(fill="x", pady=(0, 15))
        self.new_instance_btn = ctk.CTkButton(btn_frame, text=self.t("new_instance"), command=self.create_instance, height=38, font=("Inter", 12, "bold"), fg_color=COLORS["primary"], corner_radius=8)
        self.new_instance_btn.pack(side="left", padx=(0, 10))
        self.import_instance_btn = ctk.CTkButton(btn_frame, text=self.t("import_instance"), command=self.import_instance, height=38, font=("Inter", 12), fg_color=COLORS["secondary"], corner_radius=8)
        self.import_instance_btn.pack(side="left")
        
        self.instances_frame = ctk.CTkScrollableFrame(page, fg_color="transparent")
        self.instances_frame.pack(fill="both", expand=True)
        
        self.pages["instances"] = page
    
    def create_settings_page(self):
        page = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        page.pack(fill="both", expand=True)
        
        self.settings_title = ctk.CTkLabel(page, text=self.t("settings_title"), font=("Inter", 24, "bold"), text_color=COLORS["text"])
        self.settings_title.pack(anchor="w", pady=(0, 20))
        
        grid = ctk.CTkFrame(page, fg_color="transparent")
        grid.pack(fill="both", expand=True)
        grid.grid_columnconfigure(0, weight=1)
        grid.grid_columnconfigure(1, weight=1)
        
        general = ctk.CTkFrame(grid, fg_color=COLORS["card"], corner_radius=12)
        general.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=5)
        self.general_title = ctk.CTkLabel(general, text=self.t("general"), font=("Inter", 14, "bold"), text_color=COLORS["text_secondary"])
        self.general_title.pack(anchor="w", padx=20, pady=(20, 15))
        
        self.theme_label = ctk.CTkLabel(general, text=self.t("theme"), font=("Inter", 12))
        self.theme_label.pack(anchor="w", padx=20)
        self.theme_menu = ctk.CTkOptionMenu(general, values=["Dark", "Light", "System"], width=150, height=35, font=("Inter", 11), fg_color=COLORS["bg"], command=self.change_theme)
        self.theme_menu.pack(anchor="w", padx=20, pady=(5, 15))
        self.theme_menu.set("Dark")
        
        self.lang_label = ctk.CTkLabel(general, text=self.t("language"), font=("Inter", 12))
        self.lang_label.pack(anchor="w", padx=20)
        self.lang_menu = ctk.CTkOptionMenu(general, values=["Deutsch", "English"], width=150, height=35, font=("Inter", 11), fg_color=COLORS["bg"], command=self.change_language)
        self.lang_menu.pack(anchor="w", padx=20, pady=(5, 20))
        self.lang_menu.set("Deutsch")
        
        mc = ctk.CTkFrame(grid, fg_color=COLORS["card"], corner_radius=12)
        mc.grid(row=0, column=1, sticky="nsew", padx=(10, 0), pady=5)
        self.minecraft_title = ctk.CTkLabel(mc, text=self.t("minecraft_settings"), font=("Inter", 14, "bold"), text_color=COLORS["text_secondary"])
        self.minecraft_title.pack(anchor="w", padx=20, pady=(20, 15))
        
        self.java_label = ctk.CTkLabel(mc, text=self.t("java_path"), font=("Inter", 12))
        self.java_label.pack(anchor="w", padx=20)
        java_frame = ctk.CTkFrame(mc, fg_color="transparent")
        java_frame.pack(fill="x", padx=20, pady=(5, 15))
        self.java_path_display = ctk.CTkLabel(java_frame, text=self.java_path, font=("Inter", 10), text_color=COLORS["text_muted"])
        self.java_path_display.pack(side="left", fill="x", expand=True)
        self.java_browse = ctk.CTkButton(java_frame, text=self.t("change"), width=60, height=28, font=("Inter", 10), command=self.browse_java)
        self.java_browse.pack(side="right", padx=(10, 0))
        
        self.dir_label = ctk.CTkLabel(mc, text=self.t("minecraft_dir"), font=("Inter", 12))
        self.dir_label.pack(anchor="w", padx=20)
        dir_frame = ctk.CTkFrame(mc, fg_color="transparent")
        dir_frame.pack(fill="x", padx=20, pady=(5, 20))
        self.dir_display = ctk.CTkLabel(dir_frame, text=self.minecraft_dir, font=("Inter", 10), text_color=COLORS["text_muted"])
        self.dir_display.pack(side="left", fill="x", expand=True)
        self.dir_browse = ctk.CTkButton(dir_frame, text=self.t("change"), width=60, height=28, font=("Inter", 10), command=self.browse_minecraft_dir)
        self.dir_browse.pack(side="right", padx=(10, 0))
        
        advanced = ctk.CTkFrame(grid, fg_color=COLORS["card"], corner_radius=12)
        advanced.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=10)
        self.advanced_title = ctk.CTkLabel(advanced, text=self.t("advanced"), font=("Inter", 14, "bold"), text_color=COLORS["text_secondary"])
        self.advanced_title.pack(anchor="w", padx=20, pady=(20, 15))
        
        self.jvm_label = ctk.CTkLabel(advanced, text=self.t("jvm_args"), font=("Inter", 12))
        self.jvm_label.pack(anchor="w", padx=20)
        self.jvm_args_entry = ctk.CTkEntry(advanced, placeholder_text="-XX:+UseG1GC", height=35, fg_color=COLORS["bg"])
        self.jvm_args_entry.pack(fill="x", padx=20, pady=(5, 15))
        
        self.logging_label = ctk.CTkLabel(advanced, text=self.t("logging"), font=("Inter", 12))
        self.logging_label.pack(anchor="w", padx=20)
        self.logging_var = ctk.BooleanVar(value=True)
        self.logging_check = ctk.CTkCheckBox(advanced, text=self.t("save_logs"), variable=self.logging_var, font=("Inter", 11), fg_color=COLORS["primary"])
        self.logging_check.pack(anchor="w", padx=20, pady=(5, 20))
        
        self.pages["settings"] = page
    
    def create_stats_page(self):
        page = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        page.pack(fill="both", expand=True)
        
        self.stats_title = ctk.CTkLabel(page, text=self.t("stats_title"), font=("Inter", 24, "bold"), text_color=COLORS["text"])
        self.stats_title.pack(anchor="w", pady=(0, 20))
        
        grid = ctk.CTkFrame(page, fg_color="transparent")
        grid.pack(fill="x", pady=10)
        for i in range(3):
            grid.grid_columnconfigure(i, weight=1)
        
        stats = [
            ("playtime", f"{self.playtime_minutes // 60}h {self.playtime_minutes % 60}m", COLORS["primary"]),
            ("launches", str(self.launch_count), COLORS["success"]),
            ("stats_versions", str(len(self.installed_versions)), COLORS["purple"])
        ]
        self.stats_cards = {}
        for i, (key, val, color) in enumerate(stats):
            card = ctk.CTkFrame(grid, fg_color=COLORS["card"], corner_radius=12)
            card.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
            title = ctk.CTkLabel(card, text=self.t(key), font=("Inter", 12), text_color=COLORS["text_muted"])
            title.pack(pady=(15, 5))
            value = ctk.CTkLabel(card, text=val, font=("Inter", 28, "bold"), text_color=color)
            value.pack(pady=(0, 15))
            self.stats_cards[key] = value
        
        system = ctk.CTkFrame(page, fg_color=COLORS["card"], corner_radius=12)
        system.pack(fill="x", pady=10)
        self.system_title = ctk.CTkLabel(system, text=self.t("system_info"), font=("Inter", 14, "bold"), text_color=COLORS["text_secondary"])
        self.system_title.pack(anchor="w", padx=20, pady=(15, 10))
        info = f"""{self.t("os")}: {os.name}
{self.t("python_version")}: 3.13
{self.t("launcher_version")}: 2.0
{self.t("minecraft_path")}: {self.minecraft_dir}
{self.t("java_version")}: {os.path.basename(self.java_path)}"""
        self.system_text = ctk.CTkLabel(system, text=info, font=("Inter", 11), text_color=COLORS["text_muted"], justify="left")
        self.system_text.pack(anchor="w", padx=20, pady=(0, 15))
        
        logs = ctk.CTkFrame(page, fg_color=COLORS["card"], corner_radius=12)
        logs.pack(fill="both", expand=True, pady=10)
        self.logs_title = ctk.CTkLabel(logs, text=self.t("recent_logs"), font=("Inter", 14, "bold"), text_color=COLORS["text_secondary"])
        self.logs_title.pack(anchor="w", padx=20, pady=(15, 10))
        self.logs_text = ctk.CTkTextbox(logs, font=("Inter", 10), fg_color=COLORS["bg"], height=150)
        self.logs_text.pack(fill="both", expand=True, padx=20, pady=(0, 15))
        
        self.pages["stats"] = page
    
    def display_modpacks(self):
        for widget in self.modpacks_grid.winfo_children():
            widget.destroy()
        
        filter_val = self.modpack_filter.get()
        filtered = self.modpacks if filter_val == "Alle" else [m for m in self.modpacks if m["category"] == filter_val]
        
        if not filtered:
            empty = ctk.CTkLabel(self.modpacks_grid, text="Keine Mods in dieser Kategorie", font=("Inter", 14), text_color=COLORS["text_muted"])
            empty.grid(row=0, column=0, columnspan=4, pady=50)
            return
        
        for i, pack in enumerate(filtered):
            row, col = i // 4, i % 4
            card = ctk.CTkFrame(self.modpacks_grid, fg_color=COLORS["card"], corner_radius=12)
            card.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")
            
            ctk.CTkLabel(card, text=pack["icon"], font=("Inter", 32)).pack(pady=(12, 5))
            ctk.CTkLabel(card, text=pack["name"], font=("Inter", 12, "bold"), text_color=COLORS["text"]).pack()
            info = ctk.CTkFrame(card, fg_color="transparent")
            info.pack(pady=(5, 0))
            ctk.CTkLabel(info, text=pack["version"], font=("Inter", 9), text_color=COLORS["text_muted"]).pack(side="left", padx=2)
            loader_color = COLORS["primary"] if pack["loader"] == "Forge" else COLORS["purple"] if pack["loader"] == "Fabric" else COLORS["cyan"]
            ctk.CTkLabel(info, text=pack["loader"], font=("Inter", 8, "bold"), text_color=loader_color).pack(side="left", padx=2)
            ctk.CTkLabel(card, text=pack["description"][:30] + ("..." if len(pack["description"]) > 30 else ""), font=("Inter", 9), text_color=COLORS["text_secondary"]).pack(pady=(5, 0))
            ctk.CTkLabel(card, text=f"⬇️ {pack['downloads']}", font=("Inter", 8), text_color=COLORS["text_muted"]).pack(pady=(5, 0))
            ctk.CTkButton(card, text=self.t("install_modpack"), width=100, height=28, font=("Inter", 10), fg_color=COLORS["primary"], command=lambda p=pack: self.install_modpack(p)).pack(pady=(10, 12))
    
    def filter_modpacks(self, val):
        self.display_modpacks()
    
    def load_modpacks(self):
        self.modpacks = MODPACKS_DB.copy()
        self.display_modpacks()
    
    def download_mod_from_modrinth(self, mod_id, version, loader):
        """Mod von Modrinth herunterladen"""
        try:
            api_url = f"https://api.modrinth.com/v2/project/{mod_id}/version"
            response = requests.get(api_url, timeout=10)
            if response.status_code == 200:
                versions = response.json()
                for v in versions:
                    if v["game_versions"][0] == version and loader.lower() in [l.lower() for l in v["loaders"]]:
                        for file in v["files"]:
                            return file["url"]
            return None
        except Exception as e:
            print(f"Modrinth Download Fehler: {e}")
            return None
    
    def install_modpack(self, pack):
        """Modpack wirklich installieren"""
        def install_thread():
            try:
                mod_folder = os.path.join(self.minecraft_dir, "mods")
                os.makedirs(mod_folder, exist_ok=True)
                
                self.window.after(0, lambda: messagebox.showinfo(
                    "Installiere Mod",
                    f"📦 {pack['name']}\n\nVersion: {pack['version']}\nLoader: {pack['loader']}\n\nDownload wird gestartet..."
                ))
                
                if "modrinth_id" in pack:
                    download_url = self.download_mod_from_modrinth(pack["modrinth_id"], pack["version"], pack["loader"])
                    if download_url:
                        response = requests.get(download_url, stream=True, timeout=30)
                        filename = f"{pack['name'].replace(' ', '_').replace('🔊', '').replace('📦', '').replace('🗺️', '').replace('📊', '').replace('🔍', '').replace('✨', '').strip()}_{pack['version']}.jar"
                        filepath = os.path.join(mod_folder, filename)
                        
                        with open(filepath, "wb") as f:
                            for chunk in response.iter_content(chunk_size=8192):
                                f.write(chunk)
                        
                        self.window.after(0, lambda: messagebox.showinfo(
                            self.t("success"), 
                            f"✅ {pack['name']} wurde erfolgreich installiert!\n\nSpeicherort: {mod_folder}\n\nStarte Minecraft neu, um die Mod zu aktivieren."
                        ))
                        return
                
                self.window.after(0, lambda: messagebox.showinfo(
                    "Manuelle Installation",
                    f"📦 {pack['name']}\n\nLade die Mod manuell herunter:\n🔗 https://modrinth.com/mod/{pack.get('modrinth_id', pack['name'].lower().replace(' ', '-'))}\n\nVersion: {pack['version']}\nLoader: {pack['loader']}\n\nLege die .jar Datei in:\n📁 {mod_folder}"
                ))
                
            except Exception as e:
                self.window.after(0, lambda: messagebox.showerror(self.t("error"), f"Fehler bei der Installation:\n{str(e)}"))
        
        threading.Thread(target=install_thread, daemon=True).start()
    
    def update_all_texts(self):
        nav_map = {"dashboard":"nav_dashboard","play":"nav_play","skin":"nav_skin","versions":"nav_versions","modpacks":"nav_modpacks","instances":"nav_instances","settings":"nav_settings","stats":"nav_stats"}
        for k, tk in nav_map.items():
            if k in self.nav_buttons:
                self.nav_buttons[k].configure(text=self.t(tk))
        if hasattr(self, 'welcome_label'): self.welcome_label.configure(text=self.t("welcome"))
        if hasattr(self, 'news_header'): self.news_header.configure(text=self.t("minecraft_news"))
        if hasattr(self, 'quick_label'): self.quick_label.configure(text=self.t("quick_start"))
        if hasattr(self, 'quick_play_btn'): self.quick_play_btn.configure(text=self.t("quick_play"))
        if hasattr(self, 'quick_skin_btn'): self.quick_skin_btn.configure(text=self.t("quick_skin"))
        if hasattr(self, 'play_title'): self.play_title.configure(text=self.t("play_title"))
        if hasattr(self, 'play_player_title'): self.play_player_title.configure(text=self.t("player"))
        if hasattr(self, 'play_version_title'): self.play_version_title.configure(text=self.t("version"))
        if hasattr(self, 'play_instance_title'): self.play_instance_title.configure(text=self.t("instance"))
        if hasattr(self, 'play_ram_title'): self.play_ram_title.configure(text=self.t("ram"))
        if hasattr(self, 'play_java_title'): self.play_java_title.configure(text=self.t("java"))
        if hasattr(self, 'play_options_title'): self.play_options_title.configure(text=self.t("options"))
        if hasattr(self, 'fullscreen_check'): self.fullscreen_check.configure(text=self.t("fullscreen"))
        if hasattr(self, 'visibility_check'): self.visibility_check.configure(text=self.t("close_launcher"))
        if hasattr(self, 'play_start_btn'): self.play_start_btn.configure(text=self.t("start_game"))
        if hasattr(self, 'play_status'): self.play_status.configure(text=self.t("ready"))
        if hasattr(self, 'skin_title'): self.skin_title.configure(text=self.t("skin_title"))
        if hasattr(self, 'skin_preview_title'): self.skin_preview_title.configure(text=self.t("skin_preview"))
        if hasattr(self, 'skin_manage_title'): self.skin_manage_title.configure(text=self.t("skin_management"))
        if hasattr(self, 'select_skin_btn'): self.select_skin_btn.configure(text=self.t("select_skin"))
        if hasattr(self, 'skin_upload_btn'): self.skin_upload_btn.configure(text=self.t("upload_skin"))
        if hasattr(self, 'saved_skins_title'): self.saved_skins_title.configure(text=self.t("saved_skins"))
        if hasattr(self, 'steve_skin_btn'): self.steve_skin_btn.configure(text=self.t("steve"))
        if hasattr(self, 'alex_skin_btn'): self.alex_skin_btn.configure(text=self.t("alex"))
        if hasattr(self, 'versions_title'): self.versions_title.configure(text=self.t("versions_title"))
        if hasattr(self, 'installed_title'): self.installed_title.configure(text=self.t("installed_versions"))
        if hasattr(self, 'available_title'): self.available_title.configure(text=self.t("available_versions"))
        if hasattr(self, 'search_btn'): self.search_btn.configure(text=self.t("search"))
        if hasattr(self, 'modpacks_title'): self.modpacks_title.configure(text=self.t("modpacks_title"))
        if hasattr(self, 'filter_label'): self.filter_label.configure(text=self.t("category"))
        if hasattr(self, 'refresh_btn'): self.refresh_btn.configure(text=self.t("refresh"))
        if hasattr(self, 'instances_title'): self.instances_title.configure(text=self.t("instances_title"))
        if hasattr(self, 'new_instance_btn'): self.new_instance_btn.configure(text=self.t("new_instance"))
        if hasattr(self, 'import_instance_btn'): self.import_instance_btn.configure(text=self.t("import_instance"))
        if hasattr(self, 'settings_title'): self.settings_title.configure(text=self.t("settings_title"))
        if hasattr(self, 'general_title'): self.general_title.configure(text=self.t("general"))
        if hasattr(self, 'theme_label'): self.theme_label.configure(text=self.t("theme"))
        if hasattr(self, 'lang_label'): self.lang_label.configure(text=self.t("language"))
        if hasattr(self, 'minecraft_title'): self.minecraft_title.configure(text=self.t("minecraft_settings"))
        if hasattr(self, 'java_label'): self.java_label.configure(text=self.t("java_path"))
        if hasattr(self, 'java_browse'): self.java_browse.configure(text=self.t("change"))
        if hasattr(self, 'dir_label'): self.dir_label.configure(text=self.t("minecraft_dir"))
        if hasattr(self, 'dir_browse'): self.dir_browse.configure(text=self.t("change"))
        if hasattr(self, 'advanced_title'): self.advanced_title.configure(text=self.t("advanced"))
        if hasattr(self, 'jvm_label'): self.jvm_label.configure(text=self.t("jvm_args"))
        if hasattr(self, 'logging_label'): self.logging_label.configure(text=self.t("logging"))
        if hasattr(self, 'logging_check'): self.logging_check.configure(text=self.t("save_logs"))
        if hasattr(self, 'stats_title'): self.stats_title.configure(text=self.t("stats_title"))
        if hasattr(self, 'system_title'): self.system_title.configure(text=self.t("system_info"))
        if hasattr(self, 'logs_title'): self.logs_title.configure(text=self.t("recent_logs"))
        if hasattr(self, 'user_status_label'):
            self.user_status_label.configure(text=self.t("logged_in") if self.is_logged_in else self.t("not_logged_in"))
        self.update_play_page()
        self.load_instances()
        self.display_modpacks()
    
    def show_page(self, name):
        for k, btn in self.nav_buttons.items():
            btn.configure(fg_color=COLORS["card_hover"] if k == name else "transparent")
        for p in self.pages.values():
            p.pack_forget()
        self.pages[name].pack(fill="both", expand=True)
        if name == "dashboard":
            self.update_dashboard_stats()
        elif name == "versions":
            self.update_installed_versions_list()
            self.update_available_versions_list()
        elif name == "instances":
            self.load_instances()
        elif name == "play":
            self.update_play_page()
    
    def update_dashboard_stats(self):
        self.stats_labels["stats_versions"].configure(text=str(len(self.installed_versions)))
        self.stats_labels["stats_modpacks"].configure(text=str(len(self.modpacks)))
        self.stats_labels["stats_instances"].configure(text=str(len(self.instances)))
        self.stats_labels["stats_player"].configure(text=self.user_name_label.cget("text"))
        if hasattr(self, 'stats_cards') and "stats_versions" in self.stats_cards:
            self.stats_cards["stats_versions"].configure(text=str(len(self.installed_versions)))
    
    def update_play_page(self):
        self.play_player_name.configure(text=self.user_name_label.cget("text"))
        self.play_player_status.configure(text=self.t("logged_in") if self.is_logged_in else self.t("not_logged_in"), text_color=COLORS["success"] if self.is_logged_in else COLORS["text_muted"])
        if self.versions:
            self.play_version_menu.configure(values=self.versions)
            self.play_version_menu.set(self.versions[0] if self.versions else "Lade Versionen...")
        instances = ["Standard"] + [i["name"] for i in self.instances]
        self.play_instance_menu.configure(values=instances)
        self.play_instance_menu.set("Standard")
    
    def update_ram_label(self, val):
        self.play_ram_label.configure(text=f"{int(val)/1024:.1f} GB")
    
    def set_skin_model(self, model):
        self.skin_model_var.set(model)
        self.steve_skin_btn.configure(fg_color=COLORS["primary"] if model == "CLASSIC" else COLORS["secondary"])
        self.alex_skin_btn.configure(fg_color=COLORS["primary"] if model == "SLIM" else COLORS["secondary"])
    
    def select_skin(self):
        path = filedialog.askopenfilename(title=self.t("select_skin"), filetypes=[("PNG", "*.png")])
        if path:
            self.selected_skin_path = path
            try:
                img = Image.open(path).resize((120, 120))
                ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(120, 120))
                self.skin_preview_label.configure(image=ctk_img, text="")
                self.skin_preview_label.image = ctk_img
            except:
                self.skin_preview_label.configure(text="🎨\nSkin geladen", font=("Inter", 24))
            shutil.copy(path, os.path.join(self.skins_dir, os.path.basename(path)))
            self.skin_name_label.configure(text=os.path.basename(path)[:30])
            self.load_saved_skins()
            if self.is_logged_in:
                self.skin_upload_btn.configure(state="normal")
    
    def load_saved_skins(self):
        for w in self.skins_scroll.winfo_children():
            w.destroy()
        if not os.path.exists(self.skins_dir):
            return
        skins = [f for f in os.listdir(self.skins_dir) if f.endswith(".png")]
        if not skins:
            ctk.CTkLabel(self.skins_scroll, text=self.t("no_skins"), font=("Inter", 11), text_color=COLORS["text_muted"]).pack(pady=20)
            return
        for sf in skins:
            f = ctk.CTkFrame(self.skins_scroll, fg_color=COLORS["surface"], corner_radius=8)
            f.pack(pady=3, padx=5, fill="x")
            try:
                img = Image.open(os.path.join(self.skins_dir, sf)).resize((40, 40))
                ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(40, 40))
                ctk.CTkLabel(f, image=ctk_img, text="").pack(side="left", padx=10, pady=5)
            except:
                ctk.CTkLabel(f, text="🎨", font=("Inter", 20)).pack(side="left", padx=10, pady=5)
            ctk.CTkLabel(f, text=sf[:20] + ("..." if len(sf) > 20 else ""), font=("Inter", 11)).pack(side="left", padx=10)
            ctk.CTkButton(f, text="Laden", width=60, height=28, font=("Inter", 10), fg_color=COLORS["primary"], command=lambda p=os.path.join(self.skins_dir, sf): self.load_skin_from_file(p)).pack(side="right", padx=10)
    
    def load_skin_from_file(self, path):
        self.selected_skin_path = path
        try:
            img = Image.open(path).resize((120, 120))
            ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(120, 120))
            self.skin_preview_label.configure(image=ctk_img, text="")
            self.skin_preview_label.image = ctk_img
        except:
            self.skin_preview_label.configure(text="🎨\nSkin geladen", font=("Inter", 24))
        self.skin_name_label.configure(text=os.path.basename(path)[:30])
        if self.is_logged_in:
            self.skin_upload_btn.configure(state="normal")
    
    def upload_skin(self):
        if not self.is_logged_in:
            messagebox.showerror(self.t("error"), self.t("login_first"))
            return
        if not self.selected_skin_path:
            messagebox.showerror(self.t("error"), self.t("select_skin_first"))
            return
        self.skin_upload_btn.configure(state="disabled", text="Hochladen...")
        def up():
            try:
                url = "https://api.minecraftservices.com/minecraft/profile/skins"
                headers = {"Authorization": f"Bearer {self.login_data['access_token']}"}
                with open(self.selected_skin_path, "rb") as f:
                    files = {"file": (os.path.basename(self.selected_skin_path), f, "image/png")}
                    data = {"variant": self.skin_model_var.get()}
                    r = requests.post(url, headers=headers, files=files, data=data)
                if r.status_code in [200, 204]:
                    self.window.after(0, lambda: messagebox.showinfo(self.t("success"), self.t("skin_uploaded")))
                else:
                    self.window.after(0, lambda: messagebox.showerror(self.t("error"), f"Fehler: {r.status_code}"))
            except Exception as e:
                self.window.after(0, lambda: messagebox.showerror(self.t("error"), str(e)))
            finally:
                self.window.after(0, lambda: self.skin_upload_btn.configure(state="normal", text=self.t("upload_skin")))
        threading.Thread(target=up, daemon=True).start()
    
    def load_versions(self):
        try:
            all_versions = mll.utils.get_version_list()
            self.versions = [v["id"] for v in all_versions[:50]]
            if self.versions:
                self.play_version_menu.configure(values=self.versions)
                self.play_version_menu.set(self.versions[0])
        except Exception as e:
            print(f"Fehler: {e}")
    
    def load_installed_versions(self):
        try:
            self.installed_versions = mll.utils.get_installed_versions(self.minecraft_dir)
        except Exception as e:
            print(f"Fehler: {e}")
    
    def update_installed_versions_list(self):
        for w in self.installed_scroll.winfo_children():
            w.destroy()
        if not self.installed_versions:
            ctk.CTkLabel(self.installed_scroll, text=self.t("no_versions"), font=("Inter", 11), text_color=COLORS["text_muted"]).pack(pady=20)
            return
        for v in self.installed_versions:
            f = ctk.CTkFrame(self.installed_scroll, fg_color=COLORS["surface"], corner_radius=8)
            f.pack(pady=3, padx=5, fill="x")
            ctk.CTkLabel(f, text=f"📦 {v['id']}", font=("Inter", 12)).pack(side="left", padx=10, pady=8)
            ctk.CTkLabel(f, text=v.get('type', 'release'), font=("Inter", 10), text_color=COLORS["text_muted"]).pack(side="right", padx=10)
            ctk.CTkButton(f, text=self.t("repair"), width=70, height=28, font=("Inter", 10), fg_color=COLORS["warning"], command=lambda v2=v['id']: self.repair_version(v2)).pack(side="right", padx=5)
    
    def update_available_versions_list(self, filter_text=""):
        for w in self.available_scroll.winfo_children():
            w.destroy()
        filtered = [v for v in self.versions if filter_text.lower() in v.lower()] if filter_text else self.versions
        for v in filtered[:30]:
            f = ctk.CTkFrame(self.available_scroll, fg_color=COLORS["surface"], corner_radius=8)
            f.pack(pady=3, padx=5, fill="x")
            ctk.CTkLabel(f, text=f"📦 {v}", font=("Inter", 12)).pack(side="left", padx=10, pady=8)
            installed = any(v2["id"] == v for v2 in self.installed_versions)
            if installed:
                ctk.CTkLabel(f, text=self.t("installed"), font=("Inter", 10), text_color=COLORS["success"]).pack(side="right", padx=10)
            else:
                ctk.CTkButton(f, text=self.t("install"), width=80, height=28, font=("Inter", 10), fg_color=COLORS["primary"], command=lambda v2=v: self.install_version(v2)).pack(side="right", padx=5)
    
    def filter_versions(self, text):
        self.update_available_versions_list(text)
    
    def install_version(self, version):
        def inst():
            try:
                self.version_status.configure(text=f"Installiere {version}...")
                self.version_progress.set(0.2)
                cb = {"setStatus": lambda t: self.window.after(0, lambda: self.version_status.configure(text=t)), "setProgress": lambda p: self.window.after(0, lambda: self.version_progress.set(p/100))}
                mll.install.install_minecraft_version(version, self.minecraft_dir, callback=cb)
                self.version_progress.set(1)
                self.version_status.configure(text=f"✅ {version} installiert!")
                self.window.after(2000, lambda: self.version_status.configure(text=""))
                self.load_installed_versions()
                self.update_installed_versions_list()
                self.update_available_versions_list()
            except Exception as e:
                self.window.after(0, lambda: messagebox.showerror(self.t("error"), str(e)))
        threading.Thread(target=inst, daemon=True).start()
    
    def repair_version(self, version):
        if messagebox.askyesno(self.t("repair"), f"Möchtest du {version} neu installieren?"):
            self.install_version(version)
    
    def load_instances(self):
        for w in self.instances_frame.winfo_children():
            w.destroy()
        if not self.instances:
            ctk.CTkLabel(self.instances_frame, text=self.t("no_instances"), font=("Inter", 12), text_color=COLORS["text_muted"]).pack(pady=50)
            return
        for inst in self.instances:
            f = ctk.CTkFrame(self.instances_frame, fg_color=COLORS["card"], corner_radius=12)
            f.pack(pady=8, padx=10, fill="x")
            ctk.CTkLabel(f, text="📁", font=("Inter", 24)).pack(side="left", padx=15, pady=10)
            info = ctk.CTkFrame(f, fg_color="transparent")
            info.pack(side="left", padx=10, fill="both", expand=True)
            ctk.CTkLabel(info, text=inst["name"], font=("Inter", 14, "bold"), text_color=COLORS["text"]).pack(anchor="w")
            ctk.CTkLabel(info, text=f"Version: {inst.get('version', '1.20.4')} | Modloader: {inst.get('loader', 'Vanilla')}", font=("Inter", 10), text_color=COLORS["text_muted"]).pack(anchor="w")
            btn_f = ctk.CTkFrame(f, fg_color="transparent")
            btn_f.pack(side="right", padx=10)
            ctk.CTkButton(btn_f, text=self.t("play"), width=80, height=32, font=("Inter", 11), fg_color=COLORS["success"], command=lambda i=inst: self.play_instance(i)).pack(side="left", padx=2)
            ctk.CTkButton(btn_f, text=self.t("edit"), width=80, height=32, font=("Inter", 11), fg_color=COLORS["secondary"], command=lambda i=inst: self.edit_instance(i)).pack(side="left", padx=2)
    
    def create_instance(self):
        d = ctk.CTkInputDialog(text="Name der Instanz:", title=self.t("new_instance"))
        name = d.get_input()
        if name:
            self.instances.append({"name": name, "version": "1.20.4", "loader": "Vanilla", "path": os.path.join(self.instances_dir, name)})
            os.makedirs(os.path.join(self.instances_dir, name), exist_ok=True)
            self.load_instances()
            messagebox.showinfo(self.t("success"), self.t("instance_created"))
    
    def import_instance(self):
        folder = filedialog.askdirectory(title="Instanz Ordner auswählen")
        if folder:
            self.instances.append({"name": os.path.basename(folder), "version": "1.20.4", "loader": "Vanilla", "path": folder})
            self.load_instances()
            messagebox.showinfo(self.t("success"), self.t("instance_imported"))
    
    def play_instance(self, inst):
        messagebox.showinfo("Info", f"Starte Instanz {inst['name']}...\n(Demo-Funktion)")
    
    def edit_instance(self, inst):
        messagebox.showinfo("Info", f"Bearbeite Instanz {inst['name']}...\n(Demo-Funktion)")
    
    def check_news(self):
        try:
            r = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json", timeout=5)
            data = r.json()
            news = f"{self.t('minecraft_news')}\n\n" + "\n".join([f"• {v['type'].upper()}: {v['id']}" for v in data.get("versions", [])[:10]])
            self.news_text.configure(state="normal")
            self.news_text.delete("1.0", "end")
            self.news_text.insert("1.0", news)
            self.news_text.configure(state="disabled")
        except:
            self.news_text.configure(state="normal")
            self.news_text.delete("1.0", "end")
            self.news_text.insert("1.0", "Keine Verbindung zum News-Server.")
            self.news_text.configure(state="disabled")
    
    def microsoft_login(self):
        self.login_btn.configure(state="disabled", text="Login...")
        def login():
            try:
                url, state, code = ms_account.get_secure_login_data(None, "http://localhost:8080")
                webbrowser.open(url)
                code_url = tkinter.simpledialog.askstring("Microsoft Login", "URL einfügen:", parent=self.window)
                if code_url:
                    auth = ms_account.parse_auth_code_url(code_url, state)
                    self.login_data = ms_account.complete_login(None, None, "http://localhost:8080", auth, code)
                    self.is_logged_in = True
                    self.window.after(0, lambda: self.user_name_label.configure(text=self.login_data.get('name', 'Spieler')))
                    self.window.after(0, lambda: self.user_status_label.configure(text=self.t("logged_in"), text_color=COLORS["success"]))
                    self.window.after(0, lambda: self.login_btn.configure(text=self.t("logged_in"), state="disabled", fg_color=COLORS["success"]))
                    self.window.after(0, lambda: self.skin_upload_btn.configure(state="normal" if self.selected_skin_path else "disabled"))
                    self.window.after(0, lambda: self.update_play_page())
                    self.save_login_data()
            except Exception as e:
                self.window.after(0, lambda: messagebox.showerror(self.t("error"), str(e)))
                self.window.after(0, lambda: self.login_btn.configure(text="Anmelden", state="normal", fg_color=COLORS["primary"]))
        threading.Thread(target=login, daemon=True).start()
    
    def check_saved_login(self):
        try:
            if os.path.exists("login_cache.json"):
                with open("login_cache.json", "r") as f:
                    data = json.load(f)
                if data.get("expires_in", 0) > 0:
                    self.login_data = data
                    self.is_logged_in = True
                    self.user_name_label.configure(text=data.get('name', 'Spieler'))
                    self.user_status_label.configure(text=self.t("logged_in"), text_color=COLORS["success"])
                    self.login_btn.configure(text=self.t("logged_in"), state="disabled", fg_color=COLORS["success"])
                    self.skin_upload_btn.configure(state="normal" if self.selected_skin_path else "disabled")
        except:
            pass
    
    def save_login_data(self):
        if self.login_data:
            with open("login_cache.json", "w") as f:
                json.dump(self.login_data, f)
    
    def browse_java(self):
        p = filedialog.askopenfilename(title="Java auswählen", filetypes=[("Java", "javaw.exe")])
        if p:
            self.java_path = p
            self.java_path_display.configure(text=p)
            self.java_path_label.configure(text=f"Java: {os.path.basename(p)}")
    
    def browse_minecraft_dir(self):
        p = filedialog.askdirectory(title="Minecraft Verzeichnis")
        if p:
            self.minecraft_dir = p
            self.dir_display.configure(text=p)
    
    def change_theme(self, theme):
        if theme == "Dark": ctk.set_appearance_mode("dark")
        elif theme == "Light": ctk.set_appearance_mode("light")
        else: ctk.set_appearance_mode("system")
    
    def change_language(self, lang):
        self.current_lang = "de" if lang == "Deutsch" else "en"
        self.update_all_texts()
        self.update_play_page()
        self.update_installed_versions_list()
        self.update_available_versions_list()
        self.load_saved_skins()
        self.display_modpacks()
        self.load_instances()
    
    def is_version_installed(self, version):
        vp = os.path.join(self.minecraft_dir, "versions", version)
        return os.path.exists(os.path.join(vp, f"{version}.json")) and os.path.exists(os.path.join(vp, f"{version}.jar"))
    
    def start_minecraft(self):
        version = self.play_version_menu.get()
        if not version or version == "Lade Versionen...":
            messagebox.showerror(self.t("error"), self.t("wait_versions"))
            return
        
        ram = int(self.play_ram_slider.get())
        self.play_status.configure(text=self.t("starting"))
        self.play_start_btn.configure(state="disabled", text=self.t("starting") + "...")
        
        def launch():
            try:
                if not self.is_version_installed(version):
                    self.window.after(0, lambda: self.play_status.configure(text=f"{self.t('installing')} {version}..."))
                    mll.install.install_minecraft_version(version, self.minecraft_dir)
                
                jvm = [f"-Xmx{ram}M", f"-Xms{min(ram, 512)}M"]
                if hasattr(self, 'jvm_args_entry') and self.jvm_args_entry.get():
                    jvm.extend(self.jvm_args_entry.get().split())
                
                if self.is_logged_in and self.login_data:
                    opts = {"username": self.login_data.get("name", "Player"), "uuid": self.login_data.get("id", ""), "token": self.login_data.get("access_token", ""), "jvmArguments": jvm}
                else:
                    opts = {"username": f"Player{random.randint(1000, 9999)}", "jvmArguments": jvm}
                
                if self.fullscreen_var.get():
                    opts.setdefault("gameArguments", [])
                    opts["gameArguments"].append("--fullscreen")
                
                cmd = mll.command.get_minecraft_command(version, self.minecraft_dir, opts)
                subprocess.Popen(cmd, cwd=self.minecraft_dir)
                
                self.launch_count += 1
                self.save_stats()
                
                if self.launcher_visibility_var.get():
                    self.window.after(1000, self.window.destroy)
                else:
                    self.window.after(0, lambda: self.play_status.configure(text=self.t("running"), text_color=COLORS["success"]))
                
                if hasattr(self, 'logging_var') and self.logging_var.get():
                    log = os.path.join(self.logs_dir, f"launch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
                    with open(log, "w") as f:
                        f.write(f"Version: {version}\nRAM: {ram} MB\nCommand: {' '.join(cmd)}")
            except Exception as e:
                self.window.after(0, lambda: messagebox.showerror(self.t("error"), f"{self.t('error_start')}:\n{str(e)}"))
                self.window.after(0, lambda: self.play_status.configure(text=self.t("error_start"), text_color=COLORS["error"]))
            finally:
                if not self.launcher_visibility_var.get():
                    self.window.after(0, lambda: self.play_start_btn.configure(state="normal", text=self.t("start_game")))
                    self.window.after(5000, lambda: self.play_status.configure(text=self.t("ready"), text_color=COLORS["text_muted"]))
        
        threading.Thread(target=launch, daemon=True).start()
    
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = MinecraftLauncher()
    app.run()