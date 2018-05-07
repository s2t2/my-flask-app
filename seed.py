from app import db, Robot, rollback_and_print

seeds = [
    {"name":"c3po", "description":"specializes in language translation"},
    {"name":"r2d2", "description":"holds a secret message"},
    {"name":"bb8", "description":"rolls around"}
]

for seed in seeds:
    robot = Robot(seed)

    try:
        db.session.add(robot)
        db.session.commit()
    except Exception as e:
        rollback_and_print(e)

print("THE DATABASE HAS BEEN SEEDED")

print("THERE ARE %s ROBOTS IN THE DATABASE" % Robot.query.count())
