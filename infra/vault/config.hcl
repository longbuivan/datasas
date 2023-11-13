# Enable the AppRole authentication method
auth_enable_approle = true

# Create an AppRole for database authentication
approle "database" {
  policies = ["default"]
  secret_id_ttl = "10m"
  secret_id_num_uses = 10
  token_num_uses = 10
  token_ttl = "20m"
  token_max_ttl = "30m"
}
