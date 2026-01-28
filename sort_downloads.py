from pathlib import Path
import shutil

DOWNLOADS = Path(__file__).parent

#Structure for loop
CATEGORIES = {
    "Media/Video": [".mp4", ".mkv", ".avi", ".mov"],
    "Media/Audio": [".mp3", ".wav", ".flac", ".aac"],

    "Images/JPG": [".jpg", ".jpeg"],
    "Images/PNG": [".png"],
    "Images/GIF": [".gif"],

    "Documents/PDF": [".pdf"],
    "Documents/Word": [".doc", ".docx"],
    "Documents/Text": [".txt", ".md"],

    "Archives/ZIP": [".zip", ".rar", ".7z"],

    "Programming": [".py", ".js", ".c", ".cpp", ".java", ".rb", ".go", ".ts", ".sh",".sql"],
}

def get_target(file: Path) -> Path:
    suffix = file.suffix.lower()
    for folder, extensions in CATEGORIES.items():
        if suffix in extensions:
            return DOWNLOADS / folder
    return DOWNLOADS / "Other"

def move_file(file: Path, target_dir: Path):
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / file.name

    # skriv inte över filer
    if target_path.exists():
        return

    shutil.move(str(file), str(target_path))
    print(f"Moved: {file.name} → {target_dir.relative_to(DOWNLOADS)}")

def main():
    for item in DOWNLOADS.iterdir():
        if item.name == Path(__file__).name:
            continue
        if item.is_dir():
            continue
        if item.name.startswith("."):
            continue

        target_dir = get_target(item)
        move_file(item, target_dir)

if __name__ == "__main__":
    main()

