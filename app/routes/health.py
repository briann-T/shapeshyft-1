from fastapi import APIRouter, HTTPException, Security
from app.models.water import WaterEntries
from app.models.sleep import SleepEntries
from app.schemas.health import wEntry, wEntryResponse, wCreateResponse, sEntry, sEntryResponse, sResponse
from app.models.user import UserAccount
from app.services.auth.utils import get_current_user
from app.utils.exception import ShapeShyftException
from datetime import date,datetime, time
from  app.services.recommender.recommend import water_rec,sleep_rec

from app.utils.response import responses
from app.utils.exception import ShapeShyftException


router = APIRouter(
    tags=["Health profile"],
)

#Water
#Create water entry
@router.post("/createWater", response_model=wCreateResponse,responses=responses)
async def create_water(current_user: UserAccount = Security(get_current_user)):
    if(await WaterEntries.exists(user=current_user, date=date.today())==False):
        water = await WaterEntries.create(user=current_user, date=date.today())
        return water
    else:
        raise ShapeShyftException("E1024", 400)
    
#Get all the entries of water associated with the account.
@router.get("/getWater", response_model=list[wEntryResponse], responses=responses)
async def get_water(current_user: UserAccount = Security(get_current_user)):
    waterLog = await WaterEntries.all().filter(user=current_user)
    return waterLog 

#Update the water entry for current date.
@router.put("/updateWater", response_model=wEntryResponse, responses=responses)
async def update_water_amount(data: wEntry, current_user: UserAccount = Security(get_current_user)):
    data=data.dict()
    amount=data['amt']
    resp={}
    hydration_log = await WaterEntries.get(user=current_user,date=date.today())
    resp['rec']=water_rec(amount)
    resp['amt']=amount
    resp['date']=date.today()
    resp['time']=hydration_log.time
    hydration_log.amt = amount
    await hydration_log.save()

    return resp

#Sleep
@router.post("/createSleep", response_model=sEntryResponse,responses=responses)
async def create_sleep(current_user: UserAccount=Security(get_current_user)):
    if(await SleepEntries.exists(user=current_user, date=date.today())==False):
        sleep_log = await SleepEntries.create(user=current_user,date=date.today(), s_time=time.min, e_time=time.min)
        return sleep_log
    else:
        raise ShapeShyftException("E1024", 400)

@router.get("/getSleep", response_model=sResponse, responses=responses)
async def get_sleep(date: date, current_user: UserAccount=Security(get_current_user)):
    sleep_entry = await SleepEntries.get(user=current_user, date=date)
    if not sleep_entry:
        raise ShapeShyftException("E1023", 404)
    else:
        return sleep_entry

@router.put("/editSleep", response_model=sResponse, responses=responses)
#most likely needs error handling of start being after end time
#date format in YYYY-MM-DD
async def edit_sleep(data : sEntry, current_user: UserAccount = Security(get_current_user)):
    sleep_entry = await SleepEntries.get(user=current_user,date=data.date)
    

    if not sleep_entry:
        raise ShapeShyftException("E1023", 404)
    else:
        #expected format to be something like 12:04PM
        string1=data.s_time +" "+ date.today().strftime("%Y-%m-%d")
        string2=data.e_time +" "+ date.today().strftime("%Y-%m-%d")
        start = datetime.strptime(string1,'%I:%M%p %Y-%m-%d')
        end = datetime.strptime(string2,'%I:%M%p %Y-%m-%d')

        #calculate hours of sleep in float val
        s=start.time()
        e=end.time()
        duration=end-start
        duration_s=duration.total_seconds()
        hours=duration_s/3600
        #PM to AM check
        if(hours<0):
            hours_in=24+hours
        else:
            hours_in=hours
            
        sleep_entry.s_time=s
        sleep_entry.e_time=e
        sleep_entry.h_slept=hours_in
        await sleep_entry.save()

        resp={}
        resp['date']=date.today()
        resp['s_time']=s
        resp['e_time']=e
        resp['h_slept']=hours_in
        #still need to get age value, testing with 18 yo age.
        resp['rec']=sleep_rec(18,hours_in)
        return resp

    

#@router.get("/getSleep", response_model=sEntryResponse, responses=responses)
#async def get_sleep(date: date, current_user: UserAccount = Security(get_current_user)):
#    
#    sleepEntry = await Sleep
