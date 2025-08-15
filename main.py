extends CharacterBody3D

@export var speed: float = 5.0
@onready var nights_label: Label = %NightsLabel
var nights_left: int = 99
var game_over: bool = false

func _ready():
    update_nights_text()
        start_night_timer()

        func _physics_process(delta):
            if game_over:
                    return

                        var input_dir = Vector3.ZERO

                            if Input.is_action_pressed("ui_up"):
                                    input_dir.z -= 1
                                        if Input.is_action_pressed("ui_down"):
                                                input_dir.z += 1
                                                    if Input.is_action_pressed("ui_left"):
                                                            input_dir.x -= 1
                                                                if Input.is_action_pressed("ui_right"):
                                                                        input_dir.x += 1

                                                                            input_dir = input_dir.normalized()
                                                                                velocity = input_dir * speed
                                                                                    move_and_slide()

                                                                                    func start_night_timer():
                                                                                        var timer = Timer.new()
                                                                                            timer.name = "NightTimer"
                                                                                                timer.wait_time = 1.0
                                                                                                    timer.autostart = true
                                                                                                        timer.one_shot = false
                                                                                                            add_child(timer)
                                                                                                                timer.timeout.connect(_on_timer_timeout)

                                                                                                                func _on_timer_timeout():
                                                                                                                    if game_over:
                                                                                                                            return

                                                                                                                                nights_left -= 1
                                                                                                                                    if nights_left > 0:
                                                                                                                                            update_nights_text()
                                                                                                                                                else:
                                                                                                                                                        nights_left = 0
                                                                                                                                                                game_over = true
                                                                                                                                                                        update_nights_text()
                                                                                                                                                                                nights_label.text = "🌙 Game Over — You survived 99 nights!"

                                                                                                                                                                                func update_nights_text():
                                                                                                                                                                                    nights_label.text = "🌙 Nights Left: %d" % nights_left
