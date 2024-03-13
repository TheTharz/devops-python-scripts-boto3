variable "filename" {
  default = "/tmp/pet.txt"
  type = string
  description = "value of the file name"
}

variable "bella" {
  default = {
    name = "bella"
    color = "black"
    food = ["chicken", "beef", "cheese"]
    favorite = true
  }
  type = object({
    name = string
    color = string
    food = list(string)
    favorite = bool
  })
}

variable "kitty" {
  type = tuple([ string, number, bool])
  default = ["kitty", 3, true]
}