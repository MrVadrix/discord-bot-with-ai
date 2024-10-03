import discord, random, os, requests
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# fun tricks #
@bot.command()
async def command_list(ctx):
    await ctx.send(f"Список всех команд:")
    await ctx.send("**$random_emoji**  ->  рандомный емодзи")
    await ctx.send("**$coin_toss**  ->  кидает монетку и говорит на какой стороне упало")
    await ctx.send("**$hello**  ->  говорит привет тебе :)")
    await ctx.send("**$heh**  ->  напиши heh и число, он столько повторит heh")
    await ctx.send("**$repeat**  ->  впиши слово после комнады и ещё число сколько повторить")
    await ctx.send("**$meme**  ->  скидывает рандомный мем")
    await ctx.send("**$dog**  ->  рандомная собака")
    await ctx.send("**$duck**  ->  рандомная утка")
    await ctx.send("**$animal**  ->  рандомное животное")
    await ctx.send("**$eko_list**  ->  список команд с темой 'екология' ")

@bot.command()
async def random_emoji(ctx):
    emoji_list = ["😀","😁","😂","🤣","😎","🥱","🥳","🤓"]
    emoji_chosen = random.choice(emoji_list)
    await ctx.send(f"{emoji_chosen}")

@bot.command()
async def coin_toss(ctx):
    coin_side = random.randint(1,2)
    if coin_side == 1:
        await ctx.send(f"Монетка упала на орла!")
    elif coin_side == 2:
        await ctx.send(f"Монетка упала на режку!")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

    '''IMAGE/FILE COMMANDS'''
@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    '''API'''
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def animal(ctx):
    animal_choice = random.randint(1,2)
    if animal_choice == 1:
        image_url = get_dog_image_url()
        await ctx.send(image_url)
    elif animal_choice == 2:
        image_url = get_duck_image_url()
        await ctx.send(image_url)

    '''eko'''
eko_fact1 = "Глобальное потепление вызвано деятельностью человека, выбрасывающей парниковые газы, что приводит к устойчивому повышению средней температуры на Земле."
eko_fact2 = "Глобального потепления последствия включают повышение уровня моря, более экстремальные погодные явления, такие как волны тепла и штормы, а также нарушения экосистем и сельского хозяйства."
eko_fact3 = "Решение проблемы глобального потепления требует сокращения выбросов парниковых газов посредством устойчивых методов и перехода на возобновляемые источники энергии."

ice_glacier_fact1 = "Таяние ледников влияет на уровень мировых океанов, увеличивая его и угрожая прибрежным областям и экосистемам."
ice_glacier_fact2 = "Этот процесс ускоряется из-за выбросов парниковых газов, таких как углекислый газ, в атмосферу из-за человеческой деятельности."
ice_glacier_fact3 = "Таяние ледников происходит из-за глобального потепления, которое приводит к повышению средней температуры на Земле."

@bot.command()
async def eko_list(ctx):
    await ctx.send("Список команд, содержащих экологические аспекты:")
    await ctx.send("**$global_warming_facts**   ->   факты о глобальном потеплении")
    await ctx.send("**$ice_glaciers_melting**    ->   информация о таянии ледников")
    await ctx.send("**$global_warming_solving**  ->  способы решить глобальное потепление")

@bot.command()
async def global_warming_facts(ctx):
    global_warming_fact_chosen = random.randint(1,3)
    if global_warming_fact_chosen == 1:
        await ctx.send(f"Вот вам факт о глобальном потеплении:\n{eko_fact1}")
    if global_warming_fact_chosen == 2:
        await ctx.send(f"Вот вам факт о глобальном потеплении:\n{eko_fact2}")
    if global_warming_fact_chosen == 3:
        await ctx.send(f"Вот вам факт о глобальном потеплении:\n{eko_fact3}")

@bot.command()
async def ice_glaciers_melting(ctx):
    ice_glaciers_fact_chosen = random.randint(1,3)
    if ice_glaciers_fact_chosen == 1:
        await ctx.send(f"Вот вам факт о ледниках:\n{ice_glacier_fact1}")
    if ice_glaciers_fact_chosen == 2:
        await ctx.send(f"Вот вам факт о ледниках:\n{ice_glacier_fact2}")
    if ice_glaciers_fact_chosen == 3:
        await ctx.send(f"Вот вам факт о ледниках:\n{ice_glacier_fact3}")

@bot.command()
async def global_warming_solving(ctx):
    solving_num = random.randint(1,3)
    if solving_num == 1:
        await ctx.send(f"Вот один способ:\nПереход на возобновляемую энергию:\nИспользование солнечной, ветровой и гидроэнергии для сокращения выбросов парниковых газов.")
    if solving_num == 2:
        await ctx.send(f"Вот один способ:\nПовышение энергоэффективности:\nУлучшение энергоэффективности в зданиях, транспорте и промышленности для снижения потребления энергии.")
    if solving_num == 3:
        await ctx.send(f"Вот один способ:\nСохранение и восстановление лесов:\nЗащита лесов от вырубки и активное восстановление деградированных лесных зон для поглощения углекислого газа.")

#  AI  #

@bot.command()
async def new_command(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            
            await attachment.save(f"images/{file_name}")
            await ctx.send(f"Сохранили картинку в images/{file_name}")
            await ctx.send(get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"img/{file_name}"))
    else:
        await ctx.send("Вы забыли загрузить фотографию!")


#  ---  #

#TOKEN
bot.run(TOKEN)
