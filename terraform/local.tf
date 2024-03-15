resource "local_file" "pet" {
  filename = "tmp/pet.txt"
  content  = "I have a pet named ${random_pet.mypet.id}"
  depends_on = [ random_pet.mypet ]
}

resource "random_pet" "mypet" {
  length = 3
  prefix = "Mr. John"
  separator = "."
  
}