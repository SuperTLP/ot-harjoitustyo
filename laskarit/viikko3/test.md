title tehtävä 3

main->machine: machine()
machine->FuelTank:Fueltank()
machine->Engine:engine(Tank)
main->machine:machine.drive()
machine->Engine:engine.start()
Engine->FuelTank:tank.consume(5)
FuelTank-->Engine:
Engine-->machine:
machine->Engine:Engine.is_running()
Engine->FuelTank:tank.fuel_contents()
FuelTank-->Engine:35
Engine-->machine:true
machine->Engine:engine.use_energy()
Engine->FuelTank:tank.consume(10)
FuelTank-->Engine:
Engine-->machine:
