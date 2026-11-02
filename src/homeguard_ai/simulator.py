"""Reproducible synthetic scenario; never represents a real building."""
import argparse, json, random
from datetime import datetime, timezone
from pathlib import Path
from .core import Baseline, Observation, evaluate

def run_scenario(seed: int = 89) -> dict:
    rng = random.Random(seed)
    now = datetime.now(timezone.utc).replace(microsecond=0)
    specs = [
        (Baseline("temperature","degC",25.0,3.0,120,"floor-1/plant-room"),25.4+rng.uniform(-.4,.4),"environment"),
        (Baseline("humidity","%RH",55.0,12.0,120,"floor-2/corridor"),57.0+rng.uniform(-1,1),"water_moisture"),
        (Baseline("vibration_rms","m/s2",.012,.008,240,"floor-3/column-C"),.035,"structural")
    ]
    findings=[]
    for i,(base,value,domain) in enumerate(specs,1):
        obs=Observation(f"SIM-{seed}-{i}",f"SYNTH-{i}",domain,base.metric,round(value,5),
                        base.unit,now.isoformat(),base.location,uncertainty=.001)
        findings.append(evaluate(obs,base,now))
    return {"report_id":f"HOMEGUARD-SIM-{seed}","generated_at":now.isoformat(),
            "evidence_status":"SIMULATION-ONLY","scenario":"synthetic_three_floor_building",
            "seed":seed,"notice":"Synthetic demonstration only; not evidence about a real building.",
            "findings":findings}

def main():
    parser=argparse.ArgumentParser(description="Run HOMEGUARD synthetic scenario")
    parser.add_argument("--seed",type=int,default=89); parser.add_argument("--output",type=Path)
    args=parser.parse_args(); report=json.dumps(run_scenario(args.seed),indent=2)
    if args.output: args.output.write_text(report+"\n",encoding="utf-8")
    else: print(report)

if __name__=="__main__": main()
