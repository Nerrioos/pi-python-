from pathlib import Path
import sys
import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()


screen = pygame.display.set_mode((550, 300))
pygame.display.set_caption("н.пионино")


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

SOUNDS_DIR = PROJECT_ROOT / "sounds"
IMAGES_DIR = PROJECT_ROOT / "images"

# --- ЗАГРУЗКА КАРТИНКИ КЛАВИШИ ---
key_width, key_height = 100, 300
key_texture = None
img_path = IMAGES_DIR / "clav.jpg"

if img_path.exists():
    try:
        raw_img = pygame.image.load(str(img_path)).convert_alpha()
        key_texture = pygame.transform.scale(raw_img, (key_width, key_height))
        print("Текстура клавиш успешно загружена!")
    except pygame.error as e:
        print(f"Ошибка чтения картинки: {e}")
else:
    print(f"Предупреждение: Картинка не найдена по пути: {img_path}. Используем заливку цветом.")


sound_do = sound_re = sound_mi = sound_si = None

def load_sound(name):
    path = SOUNDS_DIR / name
    if path.exists():
        return pygame.mixer.Sound(str(path))
    print(f"Предупреждение: Звук {name} не найден в {SOUNDS_DIR}")
    return None

sound_do = load_sound("do.mp3")
sound_re = load_sound("re.mp3")
sound_mi = load_sound("mi.mp3")
sound_si = load_sound("si.mp3")

rect_do = pygame.Rect(100, 50, key_width, key_height)
rect_re = pygame.Rect(200, 50, key_width, key_height)
rect_mi = pygame.Rect(300, 50, key_width, key_height)
rect_si = pygame.Rect(400, 50, key_width, key_height)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Проверяем клик мышкой
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rect_do.collidepoint(event.pos) and sound_do:
                sound_do.play()
            elif rect_re.collidepoint(event.pos) and sound_re:
                sound_re.play()
            elif rect_mi.collidepoint(event.pos) and sound_mi:
                sound_mi.play()
            elif rect_si.collidepoint(event.pos) and sound_si:
                sound_si.play()
    # Отрисовка
    screen.fill((40, 40, 40)) 

  
    for rect in [rect_do, rect_re, rect_mi, rect_si]:
        if key_texture:
            screen.blit(key_texture, rect)
        else:
            # Белая клавиша с черной рамкой (запасной вариант)
            pygame.draw.rect(screen, (255, 255, 255), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)

    pygame.display.flip()
