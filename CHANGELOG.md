# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Placeholder for upcoming development items.

## [2.0.0] - 2026-06-13

### Added
- Rewrote frontend in React + Vite + TypeScript.
- Integrated Tauri framework for cross-platform desktop installers (Linux `.deb`, `.AppImage`, and Windows `.exe`).
- Integrated Demucs for high-quality audio stem splitting (vocals + instrumentals).
- Integrated faster-whisper for local AI time-synced lyrics (LRC) generation.
- Added dual audio output support for Singer headphones (original mix) and Audience speakers (instrumental only).
- Added playlist management support with automatic track transitions.
- Added interactive LRC lyrics editor.

### Changed
- Migrated codebase from the old pygame-based CLI to FastAPI backend and React frontend.

## [1.0.0] - 2022-10-15

### Added
- Initial release of the Python/pygame CLI karaoke player.
- Support for playing audio tracks with synced LRC files.
