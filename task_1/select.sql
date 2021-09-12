select 
	u."name" as nome,
	u.email as email,
	r.description as descricao_papel,
	c.description as descricao_permissao
from 
	public.users u
	left join public.roles r on r.id = u.role_id
	left join public.user_claims uc on uc.user_id = u.id
	left join public.claims c on c.id = uc.claim_id 
where 
	c.active = true 