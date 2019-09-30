interface UserModel {
    name,
    id,
    url,
    avatar_url,
    login,
    email,
    bio,
    user_api_url
}


interface Dependency {
    api_url,
    depending_on_repo_id,
    id,
    name
}


interface Repo {
    id,
    created_at,
    name,
    full_name,
    url,
    default_branch,
    depend_on: Dependency[],
    repo_api_url
}
