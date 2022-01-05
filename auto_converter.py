import os, re, shutil

def get_files_in_dir_with_ext(src_dir, extension):
    regex = re.compile(f".*.{extension}")
    src_files = []
    for path, _, files in os.walk(src_dir):
        for f in files:
            if regex.match(f):
                src_files.append(os.path.join(path, f))
    return src_files

# 한양대 ERICA 에서 제작한 iOS 용 카카오톡 테마를 Android에서 사용할 수 있는 카톡 테마로 변경하는 스크립트입니다.
# ktheme 파일을 zip으로 확장자를 변경 후 압축을 풀어주세요.
ios_ktheme_extract_location = "C:\\Users\\Jeongin\\Downloads\\hanyang_erica_kakkotalk\\"

# "https://t1.kakaocdn.net/kakaocorp/Service/Theme/KakaoTalk/Android_ThemeGuide_210803.zip" 에서 apeach-9.4.5-source.zip 을 압축을 풀어주세요.
android_ktheme_souce_location = "D:\\Projects\\hanyang-ktheme-android\hy-bibi\\"

# 이미지 이름 변경
ios_ktheme_image_directory = os.path.join(ios_ktheme_extract_location, "images")
for image_path in get_files_in_dir_with_ext(ios_ktheme_image_directory, "png"):
    image_name = os.path.basename(image_path).split(".")[0]

    if str(image_name).endswith("@2x") and os.path.exists(os.path.join(ios_ktheme_image_directory, f'{str(image_name).replace("@2x", "@3x")}.png')):
        continue

    new_image_name = None
    match str(image_name).removesuffix("@3x"):
        case "maintabBgImage":
            new_image_name = "theme_background_image"
        case "maintabIcoFriends":
            new_image_name = "theme_find_add_friend_button_image"
        case "maintabIcoFriendsSelected":
            new_image_name = "theme_find_add_friend_button_pressed_image"
        case "maintabIcoChats":
            new_image_name = "theme_maintab_ico_chats_image"
        case "maintabIcoChatsSelected":
            new_image_name = "theme_maintab_ico_chats_focused_image"
        case "maintabIcoFind":
            new_image_name = "theme_maintab_ico_find_image"
        case "maintabIcoFindSelected":
            new_image_name = "theme_maintab_ico_find_focused_image"
        case "maintabIcoBrowse":
            new_image_name = "theme_maintab_ico_view_image"
        case "maintabIcoBrowseSelected":
            new_image_name = "theme_maintab_ico_view_focused_image"
        case "maintabIcoPiccoma":
            new_image_name = "theme_maintab_ico_piccoma_image"
        case "maintabIcoPiccomaSelected":
            new_image_name = "theme_maintab_ico_piccoma_focused_image"
        case "maintabIcoGame":
            new_image_name = "theme_maintab_ico_shopping_image"
        case "maintabIcoGameSelected":
            new_image_name = "theme_maintab_ico_shopping_focused_image"
        case "maintabIcoMore":
            new_image_name = "theme_maintab_ico_more_image"
        case "maintabIcoMoreSelected":
            new_image_name = "theme_maintab_ico_more_focused_image"
        case "findBtnAddFriend":
            new_image_name = None
        case "profileImg01":
            new_image_name = "theme_profile_01_image"
        case "chatroomBgImage":
            new_image_name = "theme_chatroom_background_image"
        case "chatroomBubbleSend01":
            new_image_name = "theme_chatroom_bubble_me_01_image.9"
        case "chatroomBubbleSend01Selected":
            new_image_name = "theme_chatroom_bubble_me_01_image.9"
        case "chatroomBubbleSend02":
            new_image_name = "theme_chatroom_bubble_me_02_image.9"
        case "chatroomBubbleSend02Selected":
            new_image_name = "theme_chatroom_bubble_me_02_image.9"
        case "chatroomBubbleReceive01":
            new_image_name = "theme_chatroom_bubble_you_01_image.9"
        case "chatroomBubbleReceive01Selected":
            new_image_name = "theme_chatroom_bubble_you_01_image.9"
        case "chatroomBubbleReceive02":
            new_image_name = "theme_chatroom_bubble_you_02_image.9"
        case "chatroomBubbleReceive02Selected":
            new_image_name = "theme_chatroom_bubble_you_02_image.9"
        case "passcodeBgImage":
            new_image_name = "theme_passcode_background_image"
        case "passcodeImgCode01":
            new_image_name = "theme_passcode_01_image"
        case "passcodeImgCode02":
            new_image_name = "theme_passcode_02_image"
        case "passcodeImgCode03":
            new_image_name = "theme_passcode_03_image"
        case "passcodeImgCode04":
            new_image_name = "theme_passcode_04_image"
        case "passcodeImgCode01Selected":
            new_image_name = "theme_passcode_01_checked_image"
        case "passcodeImgCode02Selected":
            new_image_name = "theme_passcode_02_checked_image"
        case "passcodeImgCode03Selected":
            new_image_name = "theme_passcode_03_checked_image"
        case "passcodeImgCode04Selected":
            new_image_name = "theme_passcode_04_checked_image"
        case "passcodeKeypadPressed":
            new_image_name = "theme_passcode_background_image"
    if new_image_name:
        new_image_name_path = os.path.join(android_ktheme_souce_location, "src\\main\\theme\\drawable-xxhdpi\\", f"{new_image_name}.png")
        print(f"{image_path} -> {new_image_name_path}")
        shutil.copy(image_path, new_image_name_path)