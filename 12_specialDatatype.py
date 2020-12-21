from fastapi import FastAPI, Body
import uvicorn
from datetime import datetime,time,timedelta
from pydantic.color import Color
from pydantic.types import PaymentCardNumber,PaymentCardBrand


app=FastAPI(debug=True)

@app.post("/datetimeExpmle")
async def get_datetime(*,
                       start_datetime: datetime=Body(None),     #Body(None) make this as Optional parameter
                       end_datetime: datetime=Body(None),
                       repeat_at: time=Body(None),
                       process_after: timedelta=Body(None),):
    start_process=start_datetime+process_after
    duration=end_datetime-start_process
    return { "Start-DateTime":start_datetime,
             "End-DateTime":end_datetime,
             "Repeat-At":repeat_at,
             "Process-After":process_after,
             "Start-process":start_process,
             "Duration":duration,
             "Process-After":process_after.seconds}

@app.post("/colorExample/")
async def read_color(*,setColor:Color):
    return {
        "Color":setColor,
        "Name":setColor.as_named(),
        "Hex":setColor.as_hex(),
        "RGB":setColor.as_rgb()
    }

@app.post("/paymentCardExample")
async def get_cardNumber(*,cardNumber:PaymentCardNumber,cardBrand:PaymentCardBrand):
    return {"Card Number":cardNumber,
            "Card Brand":cardBrand}

#Enter Below input for demo
#"Card Number": "4000000000000002",
#"Card Brand": "Visa"

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)