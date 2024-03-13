resource "local_file" "pet" {
  filename = "/root/pet.txt"
  content  = "I have a pet"
}