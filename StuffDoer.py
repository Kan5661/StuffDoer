import pygame
import time
import sys
import pyautogui
import keyboard

pygame.init()
screen = pygame.display.set_mode((400, 250))
pygame.display.set_icon(pygame.image.load('png/icon.png'))
pygame.display.set_caption('Stuff Doer')
pyautogui.PAUSE = 0

# text spammer surfaces/rect
activate_button = pygame.image.load('png/activate.png')
start_stop_box = pygame.image.load('png/start_box.png')
start_stop_box_rect = start_stop_box.get_rect()
start_stop_box_rect.x, start_stop_box_rect.y = 315, 200
text1_box = pygame.image.load('png/text1.png')
text1_box_rect = text1_box.get_rect()
text1_box_rect.x, text1_box_rect.y = 8, 45
repeat_box = pygame.image.load('png/repeat_num.png')
repeat_box_rect = repeat_box.get_rect()
repeat_box_rect.x, repeat_box_rect.y = 53, 147
interval_box = pygame.image.load('png/interval_box.png')
interval_box_rect = interval_box.get_rect()
interval_box_rect.x, interval_box_rect.y = 53, 180
clear_box = pygame.image.load('png/clear_box.png')
clear_box_rect = clear_box.get_rect()
clear_box_rect.y, clear_box_rect.x = 145, 315

# clicker surfaces/rect
clear2 = pygame.image.load('png/clear2.png')
clear2_rect, clear2_rect.x, clear2_rect.y = clear2.get_rect(), 315, 145
add_click_box = pygame.image.load('png/add_click_button.png')
add_click_box_rect = add_click_box.get_rect()
add_click_box_rect.x, add_click_box_rect.y = 315, 200
repeating_box = pygame.image.load('png/repeating_true_box.png')
repeating_box_rect = repeating_box.get_rect()
repeating_box_rect.x, repeating_box_rect.y = 315, 37
clicker_repeating_box_surface = pygame.image.load('png/repeat_num.png')

# initial states
run, text_spam, text1, text2, text1box, repeat_num, repeatbox, repeat_time, intervalbox, typer_active, clicker_active = True, False, '', '', False, '0', False, '1000', False, True, False
L1, L2, L3 = 99999, 99999, 99999

click_spam, click_list, add_click, clicker_instruction = False, [], False, 'click on + button to add clicks'
click_interval, repeating_click, clicker_repeat_num, clicker_repeat_box = '0', False, '0', False


def text_lines():
    global text1, L1, L2, L3
    if text1_surface.get_rect()[2] > 358:
        L1 = len(text1[0:L1])
    if text1_line2_surface.get_rect()[2] > 358:
        L2 = len(text1[L1:L1+L2])


def event_select():
    global repeat_box, text_spam, activate_button, intervalbox, interval_box, text1_box, repeatbox, repeating_box
    # noinspection PyGlobalUndefined
    global on_off, clicker_repeat_num, clicker_repeat_box_surface
    if repeatbox:
        repeat_box = pygame.image.load('png/repeat_num_true.png')
    elif not repeatbox:
        repeat_box = pygame.image.load('png/repeat_num.png')
    if text_spam:
        activate_button = pygame.image.load('png/stop.png').convert_alpha()
    elif not text_spam:
        activate_button = pygame.image.load('png/activate.png').convert_alpha()
    if intervalbox:
        interval_box = pygame.image.load('png/interval_box_true.png')
    elif not intervalbox:
        interval_box = pygame.image.load('png/interval_box.png')
    if text1box:
        text1_box = pygame.image.load('png/text1_true.png')
    elif not text1box:
        text1_box = pygame.image.load('png/text1.png')
    if repeating_click:
        repeating_box = pygame.image.load('png/repeating_true_box.png')
        clicker_repeat_num = '999999'
    elif not repeating_click:
        repeating_box = pygame.image.load('png/repeating_false_box.png')
    if clicker_repeat_box:
        clicker_repeat_box_surface = pygame.image.load('png/repeat_num_true.png')
    else:
        clicker_repeat_box_surface = pygame.image.load('png/repeat_num.png')


def on_press_f9():
    global add_click, clicker_instruction
    if add_click:
        click_list.append(pyautogui.position())
        add_click = False
        clicker_instruction = 'press f10 to start or click + button to add more clicks'


def on_press_f10():
    global click_spam, clicker_instruction, last_time
    if len(click_list) > 0 and int(len(str(clicker_repeat_num))) > 0 and len(str(click_interval)) != 0 \
            and str(clicker_repeat_num).isdigit() and str(click_interval).isdigit() and not click_spam:
        click_spam = True
        clicker_instruction = 'press esc to stop'
        last_time = time.time()
    elif click_spam:
            click_spam = False
            clicker_instruction = 'press f10 to start or click + button to add more clicks'
    else:
        clicker_instruction = 'missing / invalid input!'


def auto_click():
    pyautogui.PAUSE = int(click_interval) / 1000
    for clicks in click_list:
        pyautogui.click(clicks)
        print(time.time())
        if not click_spam:
            break


def on_press_esc():
    global click_spam, clicker_instruction
    click_spam = False
    clicker_instruction = 'press f10 to start or click + button to add more clicks'


while run:
    while typer_active:
        # Draw stuff
        repeat_time_text = pygame.font.SysFont('arial', 12).render(repeat_time, True, (0, 0, 0))
        repeat_time_text1 = pygame.font.SysFont('arial', 12).render('Interval', True, (0, 0, 0))
        repeat_time_text2 = pygame.font.SysFont('arial', 12).render('time(ms)', True, (0, 0, 0))
        text1_line2_surface = pygame.font.SysFont('arial', 12).render(text1[L1:L1 + L2], True, (0, 0, 0))
        text1_line3_surface = pygame.font.SysFont('arial', 12).render(text1[L2 + L1:L1 + L2 + L3], True, (0, 0, 0))
        text1_surface = pygame.font.SysFont('arial', 12).render(text1[0:L1], True, (0, 0, 0))
        repeat_text = pygame.font.SysFont('arial', 12).render('Repeat   ' + str(repeat_num), True, (0, 0, 0))
        typer_surface = pygame.font.SysFont('arial', 14).render('Typer', True, (0, 0, 0))
        clicker_surface = pygame.font.SysFont('arial', 14).render('Clicker', True, (0, 0, 0))

        screen.blit(pygame.image.load('png/background.png'), (0, 0))
        screen.blit(start_stop_box, start_stop_box_rect), screen.blit(clear_box, clear_box_rect)
        screen.blit(text1_box, text1_box_rect)
        screen.blit(repeat_box, repeat_box_rect)
        screen.blit(repeat_text, (8, 150)), screen.blit(interval_box, interval_box_rect)
        screen.blit(text1_surface, (15, 70)), screen.blit(text1_line2_surface, (15, 90))
        screen.blit(text1_line3_surface, (15, 110))
        screen.blit(repeat_time_text1, (5, 177)), screen.blit(repeat_time_text2, (2, 190))
        screen.blit(repeat_time_text, (56, 183))
        screen.blit(activate_button, (343, 210))
        screen.blit(typer_surface, (16, 5)), screen.blit(clicker_surface, (83, 5))
        text_lines()
        event_select()

        # Detect events and do stuff
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(), sys.exit()
            if start_stop_box_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                if not text_spam:
                    text_spam = True
                else:
                    text_spam = False
                last_time = time.time()

            if event.type == pygame.KEYDOWN and text1box:
                if event.key == pygame.K_BACKSPACE:
                    text1 = text1[:-1]
                elif text1_line3_surface.get_rect()[2] < 358:
                    text1 += event.unicode
            if event.type == pygame.KEYDOWN and repeatbox:
                if event.key == pygame.K_BACKSPACE:
                    repeat_num = str(repeat_num)[:-1]
                elif repeat_text.get_rect()[2] < 110:
                    repeat_num += event.unicode
            if event.type == pygame.KEYDOWN and intervalbox:
                if event.key == pygame.K_BACKSPACE:
                    repeat_time = repeat_time[:-1]
                elif repeat_text.get_rect()[2] < 110:
                    repeat_time += event.unicode

            if text1_box_rect.collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                text1box = True
            if not text1_box_rect.collidepoint((pygame.mouse.get_pos())) and not clear_box_rect.collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                text1box = False
            if repeat_box_rect.collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                repeatbox = True
            if not repeat_box_rect.collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                repeatbox = False
            if interval_box_rect.collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                intervalbox = True
            if not interval_box_rect.collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                intervalbox = False
            if clear_box_rect.collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                text1 = ''
                text1box = True
            if pygame.Rect((70, 1, 68, 22)).collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                typer_active = False
                clicker_active = True

        if len(repeat_time) == 0 or repeat_time.isdigit() is False or not str(repeat_num).isdigit():
            text_spam = False
        if len(repeat_time) > 0:
            # noinspection PyUnboundLocalVariable
            if text_spam and time.time() - float(repeat_time)/1000 > last_time:
                last_time = time.time()
                if len(str(repeat_num)) == 0 or len(str(text1)) == 0 or (int(repeat_time)) == 0:
                    text_spam = False
                elif len(text1) != 0 and int(repeat_num) > 0:
                    pyautogui.write('\n' + text1 + '\n \n', interval=0)
                    repeat_num = int(repeat_num) - 1
                else:
                    text_spam = False

        pygame.display.update()

    while clicker_active:
        screen.blit(pygame.image.load('png/background_2.png'), (0, 0))
        screen.blit(interval_box, interval_box_rect)
        # noinspection PyUnboundLocalVariable
        screen.blit(clicker_repeat_box_surface, repeat_box_rect)

        typer_surface = pygame.font.SysFont('arial', 14).render('Typer', True, (0, 0, 0))
        clicker_surface = pygame.font.SysFont('arial', 14).render('Clicker', True, (0, 0, 0))
        click_num_surface = pygame.font.SysFont('arial', 12).render('Clicks : ' + str((len(click_list))), True, (0, 0, 0))
        clicker_instruction_surface = pygame.font.SysFont('arial', 12).render(clicker_instruction, True, (255,255,255))
        clicker_repeat_time_text = pygame.font.SysFont('arial', 12).render(str(click_interval), True, (0, 0, 0))
        clicker_repeat_time_text1 = pygame.font.SysFont('arial', 12).render('Interval', True, (0, 0, 0))
        clicker_repeat_time_text2 = pygame.font.SysFont('arial', 12).render('time(ms)', True, (0, 0, 0))
        # noinspection PyUnboundLocalVariable
        repeating_text_surface = pygame.font.SysFont('arial', 12).render('Repeating', True, (0, 0, 0))
        repeating_text2_surface = pygame.font.SysFont('arial', 12).render('INFINITE', True, (0, 0, 0))
        clicker_repeat_text = pygame.font.SysFont('arial', 12).render('Repeat   ' + str(clicker_repeat_num), True, (0, 0, 0))

        screen.blit(typer_surface, (16, 5)), screen.blit(clicker_surface, (83, 5))
        screen.blit(repeating_box, repeating_box_rect)
        screen.blit(clicker_repeat_text, (8, 150))
        screen.blit(clear2, clear2_rect)
        screen.blit(add_click_box, add_click_box_rect)
        screen.blit(click_num_surface, (325, 130))
        screen.blit(clicker_instruction_surface, (20, 45))
        screen.blit(clicker_repeat_time_text1, (8, 177)), screen.blit(clicker_repeat_time_text2, (5, 190)), screen.blit(clicker_repeat_time_text, (56, 183))
        screen.blit(repeating_text_surface, (320, 90)), screen.blit(repeating_text2_surface, (325, 80))

        event_select()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(), sys.exit()
            if pygame.Rect((1, 1, 68, 22)).collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                typer_active = True
                clicker_active = False

            if clear2_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                click_list.clear()
                add_click = False
                clicker_instruction = 'click on + button to add clicks'
            if add_click_box_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                add_click = True
                clicker_instruction = 'Move mouse pos and press f9 to add one click'
            if repeating_box_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                if repeating_click:
                    repeating_click = False
                elif not repeating_click:
                    repeating_click = True
            if repeat_box_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and not repeating_click:
                clicker_repeat_box = True
            if not repeat_box_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and not repeating_click:
                clicker_repeat_box = False
            if interval_box_rect.collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                intervalbox = True
            if not interval_box_rect.collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                intervalbox = False
            if event.type == pygame.KEYDOWN and intervalbox:
                if event.key == pygame.K_BACKSPACE:
                    click_interval = click_interval[:-1]
                elif clicker_repeat_time_text.get_rect()[2] < 110:
                    click_interval += event.unicode
            if event.type == pygame.KEYDOWN and clicker_repeat_box:
                if event.key == pygame.K_BACKSPACE:
                    clicker_repeat_num = str(clicker_repeat_num)[:-1]
                elif clicker_repeat_text.get_rect()[2] < 110:
                    clicker_repeat_num += event.unicode

            keyboard.add_hotkey('F10', on_press_f10)
            keyboard.add_hotkey('esc', on_press_esc)

        if add_click:
            keyboard.add_hotkey('F9', on_press_f9)
        if len(click_interval) == 0 or click_interval.isdigit() is False:
            click_spam = False

        if click_spam and repeating_click and len(str(clicker_repeat_num)) > 0:
            auto_click()
        elif click_spam and not repeating_click and int(clicker_repeat_num) > 0 and len(str(clicker_repeat_num)) > 0:
            auto_click()
            clicker_repeat_num = int(clicker_repeat_num) - 1
        else:
            click_spam = False

        pygame.display.update()

