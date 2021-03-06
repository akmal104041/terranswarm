#pragma once

enum Params{
	S_GATHER_MINERALS,
	S_BUILD_BARRACKS_DENOMINATOR,
	S_BUILD_CMD_CENTER,
	S_ATTACK,
	//S_ATTACK_NEAR,
	//S_ATTACK_MID,
	//S_ATTACK_FAR,
	S_TRAIN_SCV_DENOMINATOR,
	S_TRAIN_MEDIC_RATIO,
	S_TRAIN_MARINE,
	K_SCV_GATHER_MINERALS,
	K_SCV_REPAIR_NEAR,
	K_SCV_REPAIR_MID,
	K_SCV_REPAIR_FAR,
	K_SCV_EXPLORE,
	K_SCV_ATTACK_NEAR,
	K_SCV_ATTACK_MID,
	K_SCV_ATTACK_FAR,
	K_MARINE_EXPLORE,
	K_MARINE_ATTACK_NEAR,
	K_MARINE_ATTACK_MID,
	K_MARINE_ATTACK_FAR,
	K_GENERAL_TRAIN_SCV,
	K_GENERAL_TRAIN_MARINE,
	K_GENERAL_TRAIN_MEDIC,
	M_PACK_SIZE
};

//list of parameter names (order is the same as the previous enum)
//init is done in Parameters.cpp
const char* PARAMETER_NAMES[];

class Parameters
{
public:
	Parameters(void);
	~Parameters(void);
};
